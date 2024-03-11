import xml.etree.ElementTree as et

import pandas as pd
from optasoccer.metadata import opta_events, opta_qualifiers

__all__ = ['read_f24']

def read_f24(file_path):
    tree = et.parse(file_path)
    root = tree.getroot()
    game = root[0]
    match_id = int(game.attrib.get('id'))
    matches = {'timestamp': root.get('timestamp'),
               'match_id': match_id,
               'additional_info': game.attrib.get('additional_info'),
               'away_score': int(game.attrib.get('away_score')),
               'home_score': int(game.attrib.get('home_score')),
               'away_team_id': int(game.attrib.get('away_team_id')),
               'away_team_name': game.attrib.get('away_team_name'),
               'away_team_short': game.attrib.get('away_team_short'),
               'competition_id': int(game.attrib.get('competition_id')),
               'competition_name': game.attrib.get('competition_name'),
               'game_date': game.attrib.get('game_date'),
               'home_team_id': int(game.attrib.get('home_team_id')),
               'home_team_name': game.attrib.get('home_team_name'),
               'home_team_official': game.attrib.get('home_team_official'),
               'home_team_short': game.attrib.get('home_team_short'),
               'matchday': int(game.attrib.get('matchday')),
               'period_1_start': game.attrib.get('period_1_start'),
               'period_2_start': game.attrib.get('period_2_start'),
               'period_3_start': game.attrib.get('period_3_start'),
               'period_4_start': game.attrib.get('period_4_start'),
               'period_5_start': game.attrib.get('period_5_start'),
               'season_id': int(game.attrib.get('season_id')),
               'season_name': game.attrib.get('season_name'),
               }
    
    matches = pd.DataFrame(matches, index=[0])
    for date_col in ['timestamp', 'game_date', 'period_1_start',
                     'period_2_start', 'period_3_start', 'period_4_start', 'period_5_start']:
        matches[date_col] = pd.to_datetime(matches[date_col])

    team_map = {game.attrib.get('home_team_id'): game.attrib.get('home_team_name'),
                game.attrib.get('away_team_id'): game.attrib.get('away_team_name')}

    events = []
    qualifiers = []
    bool_qualifiers = []
    foul_qualifiers = [value for value, key in opta_qualifiers.items() if 'foul' in key]
    for event in game:
        id = int(event.attrib.get('id'))
        new_event = {'match_id': match_id,
                     'id': id,
                     'event_id': int(event.attrib.get('event_id')),
                     'type_id': int(event.attrib.get('type_id')),
                     'period_id': int(event.attrib.get('period_id')),
                     'version': int(event.attrib.get('version')),
                     'min': int(event.attrib.get('min')),
                     'sec': int(event.attrib.get('sec')),
                     'team_id': int(event.attrib.get('team_id')),
                     'team_name': team_map[event.attrib.get('team_id')],
                     'player_id': event.attrib.get('player_id'),
                     'outcome': int(event.attrib.get('outcome')),
                     'assist': event.attrib.get('assist'),
                     'keypass': event.attrib.get('keypass'),
                     'x': float(event.attrib.get('x')),
                     'y': float(event.attrib.get('y')),
                     'timestamp': event.attrib.get('timestamp'),
                     'timestamp_utc': event.attrib.get('timestamp_utc'),
                     'last_modified': event.attrib.get('last_modified'),
                     }
        
        events.append(new_event)
        for qualifier in event:
            qualifier_id = qualifier.attrib.get('qualifier_id')
            qualifier_value = qualifier.attrib.get('value', True)
            if qualifier_id in foul_qualifiers and qualifier_value == '243':
                qualifier_value = True
                qualifiers.append({'id': id,
                                   'qualifier_id': '243',
                                   'value': True})
                bool_qualifiers.append('243')
            if qualifier_id == '41' and qualifier_value == 'Injury':
                qualifier_value = True
            if qualifier_value is True:
                bool_qualifiers.append(qualifier_id)
            qualifiers.append({'id': id,
                               'qualifier_id': qualifier_id,
                               'value': qualifier_value})

    events = pd.DataFrame(events)
    events['type_name'] = events['type_id'].astype(str).map(opta_events)
    # rename the qualifiers
    qualifiers = pd.DataFrame(qualifiers)
    qualifiers = qualifiers.pivot(index='id', columns='qualifier_id', values='value')
    qualifiers = qualifiers.rename(opta_qualifiers, axis='columns')
    qualifiers = qualifiers[qualifiers.columns.sort_values()].copy()
    for col in qualifiers.columns:
        if 'timestamp' in col or 'data_collection_complete' in col:
            qualifiers[col] = pd.to_datetime(qualifiers[col])
        if 'coordinate' in col or 'pass_end_' in col or 'length' in col or 'angle' in col:
            qualifiers[col] = qualifiers[col].astype(float)
    
    # merge events and qualifiers
    events = events.merge(qualifiers, on='id', how='left', validate='1:1')
    events['timestamp'] = pd.to_datetime(events['timestamp'])
    events['timestamp_utc'] = pd.to_datetime(events['timestamp_utc'])
    events['last_modified'] = pd.to_datetime(events['last_modified'], format='%Y-%m-%dT%H:%M:%S')
    int_cols = ['assist', 'captain_player_id', 'coach_id', 'defensive_1_v_1',
                'detailed_position_id', 'early_end_cause', 'end_type', 'fantasy_assist_team',
                'fantasy_assisted_by', 'formation_slot', 'foul_intended_tackle_target',
                'injured_player_id', 'injury_time_minutes', 'keypass', 'opposite_related_event_id',
                'opposite_related_event_id_2nd', 'pass_assist', 'penalty_taker', 'player_id',
                'player_id_causing_penalty', 'players_caught_offside', 'position_side_id',
                'related_event_id', 'related_event_id_2nd', 'reviewed_event_id', 'team_formation',
                'team_kit_id', 'var_pre_review_event_type', 'var_review', 'viral']
    int_cols = list(set(int_cols).intersection(set(events.columns)))
    events[int_cols] = events[int_cols].astype('Int64')
    events.sort_values(['match_id', 'period_id', 'min', 'sec', 'timestamp'], inplace=True)
    # remove deleted events
    events = events[events['type_name'] != 'deleted_event'].copy()
    # remove empty columns
    events.dropna(how='all', axis='columns', inplace=True)
    bool_qualifiers = list(set(bool_qualifiers))
    bool_qualifiers = [v for k, v in opta_qualifiers.items() if k in bool_qualifiers]
    bool_qualifiers = list(set(bool_qualifiers).intersection(set(events.columns)))
    events[bool_qualifiers] = events[bool_qualifiers].astype('boolean')
    events.reset_index(drop=True, inplace=True)
    return events, matches
