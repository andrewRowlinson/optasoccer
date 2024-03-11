__all__ = ['opta_events', 'opta_qualifiers']

opta_events = {'1': 'pass',
               '2': 'offside_pass',
               '3': 'take_on',
               '4': 'foul',
               '5': 'out',
               '6': 'corner_awarded',
               '7': 'tackle',
               '8': 'interception',
               # '9': 'turnover',
               '10': 'save',
               '11': 'claim',
               '12': 'clearance',
               '13': 'miss',
               '14': 'post',
               '15': 'attempt_saved',
               '16': 'goal',
               '17': 'card',
               '18': 'player_off',
               '19': 'player_on',
               '20': 'player_retired',
               '21': 'player_returns',
               '22': 'player_becomes_goalkeeper',
               '23': 'goalkeeper_becomes_player',
               '24': 'condition_change',
               '25': 'official_change',
               # 26 no event
               '27': 'start_delay',
               '28': 'end_delay',
               # 29 no event
               '30': 'end',
               # 31 no event               
               '32': 'start',
               # 33 no event
               '34': 'team_set_up',
               # 35 no event
               '36': 'player_changed_jersey_number',
               '37': 'collection_end',
               '38': 'temp_goal',
               '39': 'temp_attempt',
               '40': 'formation_change',
               '41': 'punch',
               '42': 'good_skill',
               '43': 'deleted_event',
               '44': 'aerial',
               '45': 'challenge',
               # 46 no event
               # '47': 'rescinded_card'
               '49': 'ball_recovery',
               '50': 'dispossessed',
               '51': 'error',
               '52': 'keeper_pick_up',
               '53': 'cross_not_claimed',
               '54': 'smother',
               '55': 'offside_provoked',
               '56': 'shield_ball_opp',
               '57': 'foul_throw_in',
               '58': 'penalty_faced',
               '59': 'keeper_sweeper',
               '60': 'chance_missed',
               '61': 'ball_touch',
               # 62 no event
               '63': 'temp_save',
               '64': 'resume',
               '65': 'contentious_referee_decision',
               # '66': 'possession_data'
               '67': '50_50',
               '68': 'referee_drop_ball',
               # '69': 'failed_to_block',
               '70': 'injury_time_announcement',
               '71': 'coach_setup',
               # 72 no event
               # '73': 'other_ball_contact',
               '74': 'blocked_pass',
               '75': 'delayed_start',
               '76': 'early_end',
               # 77 no event
               # 78 no event
               '79': 'coverage_interruption',
               '80': 'drop_of_ball',
               '81': 'obstacle',
               '82': 'control',
               '83': 'attempted_tackle',
               '84': 'deleted_after_review',
               }

# commented out qualifiers are no longer collected
opta_qualifiers = {'1': 'long_ball',
                   '2': 'cross',
                   '3': 'pass_head',
                   '4': 'pass_through_ball',
                   '5': 'free_kick_taken',
                   '6': 'corner_taken',
                   '7': 'players_caught_offside',
                   '8': 'goal_disallowed',
                   '9': 'penalty',
                   '10': 'foul_handball',
                   '11': 'foul_6_seconds_violation',
                   '12': 'foul_dangerous_play',
                   '13': 'foul',
                   '14': 'defensive_last_line',
                   '15': 'body_part_head',
                   '16': 'shot_location_small_box_centre',
                   '17': 'shot_location_box_centre',
                   '18': 'shot_location_out_of_box_centre',
                   '19': 'shot_location_35_plus_centre',
                   '20': 'body_part_right_foot',
                   '21': 'body_part_other',
                   '22': 'regular_play',
                   '23': 'fast_break',
                   '24': 'set_piece',
                   '25': 'shot_from_corner',
                   '26': 'free_kick',
                   # 27: no qualifier
                   '28': 'own_goal',
                   '29': 'assisted',
                   '30': 'lineup_involved',
                   '31': 'yellow_card',
                   '32': 'second_yellow',
                   '33': 'red_card',
                   '34': 'foul_referee_abuse',
                   '35': 'foul_argument',
                   '36': 'foul_violent_conduct',
                   '37': 'foul_time_wasting',
                   '38': 'foul_excessive_celebration',
                   '39': 'foul_crowd_interaction',
                   '40': 'foul_other_reason',
                   '41': 'substitution_injury',
                   '42': 'substitution_tactical',
                   # 43: no qualifier
                   '44': 'player_position',
                   # '45': 'temperature',
                   # '46': 'conditions',
                   # '47': 'conditions_field_pitch',
                   # '48': 'conditions_lightings',
                   '49': 'attendance_figure',
                   # 50: no qualifier
                   # '51': 'official_position',
                   # 52: no qualifier                 
                   '53': 'injured_player_id',
                   '54': 'early_end_cause',
                   '55': 'related_event_id',
                   '56': 'zone',
                   '57': 'end_type',
                   # 58: no qualifier
                   '59': 'jersey_number',
                   '60': 'shot_location_small_box_right',
                   '61': 'shot_location_small_box_left',
                   '62': 'shot_location_box_deep_right',
                   '63': 'shot_location_box_right',
                   '64': 'shot_location_box_left',
                   '65': 'shot_location_box_deep_left',
                   '66': 'shot_location_out_of_box_deep_right',
                   '67': 'shot_location_out_of_box_right',
                   '68': 'shot_location_out_of_box_left',
                   '69': 'shot_location_out_of_box_deep_left',
                   '70': 'shot_location_35_plus_right',
                   '71': 'shot_location_35_plus_left',
                   '72': 'body_part_left_foot',
                   '73': 'shot_left_missed',
                   '74': 'shot_high_missed',
                   '75': 'shot_right_missed',
                   '76': 'shot_low_left',
                   '77': 'shot_high_left',
                   '78': 'shot_low_centre',
                   '79': 'shot_high_centre',
                   '80': 'shot_low_right',
                   '81': 'shot_high_right',
                   '82': 'shot_blocked',
                   '83': 'shot_close_left',
                   '84': 'shot_close_right',
                   '85': 'shot_close_high',
                   '86': 'shot_close_left_and_high',
                   '87': 'shot_close_right_and_high',
                   '88': 'goalkeeper_high_claim',
                   '89': 'goalkeeper_1_on_1',
                   # '90': 'deflected_save',
                   # '91': 'dive_and_deflect',
                   # '92': 'catch',
                   # '93': 'dive_and_catch',              
                   '94': 'defensive_block',
                   '95': 'foul_back_pass',
                   # '96': 'corner_situation',
                   '97': 'direct_free',
                   # 98: no qualifier
                   # 99: no qualifier                
                   '100': 'shot_six_yard_blocked',
                   '101': 'shot_saved_off_line',
                   '102': 'shot_goal_mouth_y_coordinate',
                   '103': 'shot_goal_mouth_z_coordinate',
                   # 104: no qualifier
                   # 105: no qualifier
                   # '106': 'attacking_pass',
                   '107': 'throw_in',
                   '108': 'shot_volley',
                   # '109': 'overhead',
                   # '110': 'half_volley',
                   # '111': 'diving_header',
                   # '112': 'scramble',             
                   '113': 'shot_strong',
                   '114': 'shot_weak',
                   # '115': 'rising',
                   # '116' 'dipping',               
                   # '117': 'lob',
                   # '118': 'one_bounce',
                   # '119': 'few_Bounces',
                   '120': 'shot_swerve_left',
                   '121': 'shot_swerve_right',
                   '122': 'shot_swerve_moving',
                   '123': 'goalkeeper_throw',
                   '124': 'goalkeeper_goal_kick',
                   # 125: no qualifier
                   # 126: no qualifier                  
                   '127': 'direction_of_play',
                   '128': 'goalkeeper_punch',
                   # 129: no qualifier                  
                   '130': 'team_formation',
                   '131': 'team_player_formation',
                   '132': 'foul_dive',
                   '133': 'shot_deflection',
                   # 134: no qualifier
                   # 135: no qualifier                 
                   '136': 'goalkeeper_touched',
                   '137': 'goalkeeper_saved_off_target_shot',
                   '138': 'shot_hit_woodwork',
                   '139': 'goalkeeper_save_shot_from_own_player',
                   '140': 'pass_end_x',
                   '141': 'pass_end_y',
                   # 142: no qualifier
                   # 143: no qualifier
                   '144': 'explanation_of_deleted_event',
                   '145': 'formation_slot',
                   '146': 'shot_blocked_x_coordinate',
                   '147': 'shot_blocked_y_coordinate',
                   # 148: no qualifier
                   # 149: no qualifier
                   # 150: no qualifier
                   # 151: no qualifier                
                   '152': 'free_kick_direct',
                   '153': 'shot_not_past_goal_line',
                   '154': 'shot_intentional_assist',
                   '155': 'pass_chipped',
                   '156': 'pass_lay_off',
                   '157': 'launch',
                   '158': 'foul_persistent_infringement',
                   '159': 'foul_and_abusive_language',
                   '160': 'shot_throw_in_set_piece',
                   '161': 'foul_encroachment',
                   '162': 'foul_leaving_field',
                   '163': 'foul_entering_field',
                   '164': 'foul_spitting',
                   '165': 'foul_professional_last_man',
                   '166': 'foul_professional_handball',
                   '167': 'defensive_out_of_play',
                   '168': 'pass_flick_on',
                   '169': 'defensive_error_leading_to_attempt',
                   '170': 'defensive_error_leading_to_goal',
                   '171': 'rescinded_card',
                   # 172: no qualifier
                   '173': 'goalkeeper_parried_safe',
                   '174': 'goalkeeper_parried_danger',
                   '175': 'goalkeeper_fingertip',
                   '176': 'goalkeeper_caught',
                   '177': 'goalkeeper_collected',
                   '178': 'standing',
                   '179': 'goalkeeper_save_while_diving',
                   '180': 'goalkeeper_save_while_stooping',
                   '181': 'goalkeeper_save_while_reaching',
                   '182': 'goalkeeper_saves_with_hands',
                   '183': 'goalkeeper_saves_with_feet',
                   '184': 'foul_dissent',
                   '185': 'defensive_blocked_cross',
                   '186': 'penalty_scored',
                   '187': 'penalty_saved',
                   '188': 'penalty_missed',
                   '189': 'off_camera_not_visible',
                   '190': 'goalkeeper_saved_from_shot_off_target',
                   '191': 'foul_off_the_ball',
                   '192': 'foul_block_by_hand',
                   # '193': 'goal_measure',
                   '194': 'captain_player_id',
                   '195': 'pass_pull_back',
                   '196': 'pass_switch_of_play',
                   '197': 'team_kit_id',
                   '198': 'goalkeeper_hoof',
                   '199': 'goalkeeper_kick_from_hands',
                   '200': 'referee_stops_play',
                   '201': 'referee_delay',
                   '202': 'stoppage_weather_problem',
                   '203': 'stoppage_crowd_trouble',
                   '204': 'stoppage_fire',
                   '205': 'stoppage_object_thrown_on_pitch',
                   '206': 'stoppage_spectator_on_pitch',
                   '207': 'stoppage_awaiting_officials_decision',
                   '208': 'stoppage_referee_injury',
                   '209': 'game_end',
                   '210': 'pass_assist',
                   '211': 'take_on_overrun',
                   '212': 'length',
                   '213': 'angle',
                   '214': 'shot_big_chance',
                   '215': 'shot_individual_play',
                   '216': 'related_event_id_2nd',
                   '217': 'shot_2nd_assisted',
                   '218': 'pass_2nd_assist',
                   '219': 'corner_player_on_both_posts',
                   '220': 'corner_player_on_near_post',
                   '221': 'corner_player_on_far_post',
                   '222': 'corner_no_players_on_posts',
                   '223': 'in_swinger',
                   '224': 'out_swinger',
                   '225': 'straight',
                   '226': 'stoppage_game_suspended',
                   '227': 'stoppage_game_resumed',
                   '228': 'shot_blocked_own_teammate',
                   '229': 'post_match_complete',
                   '230': 'goalkeeper_x_coordinate',
                   '231': 'goalkeeper_y_coordinate',
                   '232': 'goalkeeper_smother_unchallenged',
                   '233': 'opposite_related_event_id',
                   '234': 'home_team_possession',
                   '235': 'away_team_possession',
                   '236': 'pass_blocked',
                   '237': 'goalkeeper_low_goal_kick',
                   '238': 'fair_play',
                   '239': 'defensive_block_by_wall',
                   '240': 'goalkeeper_from_ground_after_collected_with_hands',
                   '241': 'freekick_indirect',
                   '242': 'foul_obstruction',
                   '243': 'foul_unsporting_behaviour',
                   '244': 'foul_not_retreating',
                   '245': 'foul_serious',
                   '246': 'stoppage_drinks_break',
                   '247': 'referee_contentious_offside',
                   '248': 'referee_contentious_goal_line',
                   '249': 'pending_shot',
                   '250': 'pending_blocked',
                   '251': 'pending_shot_post',
                   '252': 'pending_shot_missed',
                   '253': 'pending_shot_missed_not_passed_goal_line',
                   '254': 'goal_follows_a_dribble',
                   # '255': 'conditions_open_roof',
                   # '256': 'conditions_air_humidity',
                   # '257': 'conditions_air_pressure',
                   # '258': 'conditions_sold_out',
                   # '259': 'conditions_celsius_degrees',
                   # '260': 'conditions_floodlight',
                   # 261: no qualifier
                   # 262: no qualifier                  
                   '263': 'shot_corner_direct',
                   '264': 'foul_aerial',
                   '265': 'foul_attempted_tackle',
                   # '266': 'put_through',
                   # '267': 'right_arm',
                   # '268': 'left_arm',
                   # '269': 'both_arms',
                   # '270': 'right_leg',                   
                   # '271': 'left_Leg',
                   # '272'': 'both_Legs', 
                   '273': 'goalkeeper_save_hit_right_post',
                   '274': 'goalkeeper_save_hit_left_post',
                   '275': 'goalkeeper_save_hit_bar',
                   '276': 'shot_out_on_sideline',
                   '277': 'injury_time_minutes',
                   '278': 'tap',
                   '279': 'kick_off',
                   '280': 'fantasy_assist_type',
                   '281': 'fantasy_assisted_by',
                   '282': 'fantasy_assist_team',
                   '283': 'coach_id',
                   # 284: no qualifier
                   '285': 'duel_events_defensive',
                   '286': 'duel_events_offensive',
                   '287': 'goalkeeper_over_arm',
                   '288': 'out_of_play_secs',
                   '289': 'foul_denied_goal_scoring_opp',
                   '290': 'coach_types',
                   # 291: no qualifier
                   '292': 'detailed_position_id',
                   '293': 'position_side_id',
                   '294': 'foul_shove_push',
                   '295': 'foul_shirt_pull_holding',
                   '296': 'foul_elbow_violent_conduct',
                   '297': 'offside_pass_follows_shot_rebound',
                   '298': 'offside_pass_follows_shot_blocked',
                   '299': 'stoppage_affects_match_clock',
                   '300': 'goal_solo_run',
                   '301': 'shot_from_cross',
                   '302': 'data_collection_checks_complete',
                   '303': 'stoppage_floodlight_failure',
                   # 304: no qualifier
                   # 305: no qualifier
                   # 306: no qualifier
                   # '307': 'phase_of_possession_id',
                   '308': 'goes_to_extra_time',
                   '309': 'goes_to_penalties',
                   # 310: no qualifier
                   # 311: no qualifier
                   # '312': 'phase_of_possession_start',
                   '313': 'foul_illegal_restart',
                   '314': 'foul_end_of_offside',
                   # 315: no qualifier
                   '316': 'passed_penalty',
                   '317': 'penalty_set_piece',
                   # 318: no qualifier                
                   '319': 'captain_change',
                   # '320': 'extra_flag_for_checker',
                   # 321: no qualifier              
                   # 322: no qualifier             
                   # 323: no qualifier             
                   # 324: no qualifier             
                   '325': 'abandonment_to_follow',
                   # 326: no qualifier             
                   # 327: no qualifier                  
                   '328': 'shot_first_touch',
                   '329': 'var_goal_awarded',
                   '330': 'var_penalty_awarded',
                   '331': 'var_penalty_not_awarded',
                   '332': 'var_card_upgrade',
                   '333': 'var_mistaken_identity',
                   '334': 'var_other',
                   '335': 'var_referee_decision_confirmed',
                   '336': 'var_referee_decision_cancelled',
                   # 337: no qualifier
                   # 338: no qualifier
                   # 339: no qualifier
                   # 340: no qualifier
                   '341': 'var_goal_not_awarded',
                   '342': 'var_red_card_given',
                   '343': 'var_review',
                   '344': 'stoppage_video_coverage_lost',
                   '345': 'overhit_cross',
                   '346': 'next_event_goal_kick',
                   '347': 'next_event_throw_in',
                   '348': 'penalty_taker',
                   # 349: no qualifier
                   # 350: no qualifier
                   # 351: no qualifier
                   # 352: no qualifier
                   '353': 'opposite_related_event_id_2nd',
                   '354': 'referee_ball_hits',
                   '355': 'foul_entering_referee_review_area',
                   '356': 'foul_excessive_usage_of_review_signal',
                   '357': 'foul_entering_video_operations_room',
                   '358': 'official_body_reviewed_and_confirmed',
                   '359': 'official_body_review_and_changed',
                   # 360: no qualifier
                   '361': 'incorrect_out_of_play_decision',
                   '362': 'viral',
                   '363': 'away_attendance',
                   '364': 'var_delay',
                   '365': 'reviewed_event_id',
                   # 366: no qualifier
                   # 367: no qualifier
                   # 368: no qualifier
                   # 369: no qualifier
                   # 370: no qualifier
                   # 371: no qualifier
                   # 372: no qualifier
                   # 373: no qualifier
                   '374': 'goal_shot_timestamp',
                   '375': 'goal_shot_game_clock',
                   '376': 'goalkeeper_intervention_low',
                   '377': 'goalkeeper_intervention_medium',
                   '378': 'goalkeeper_intervention_high',
                   # 379: no qualifier
                   '380': 'ball_hits_other_obstacle',
                   '381': 'goalkeeper_fumble',
                   # 382: no qualifier
                   '383': 'defensive_touch_type_control',
                   '384': 'defensive_touch_type_pass',
                   '385': 'defensive_touch_type_clearance',
                   '386': 'driven_cross',
                   '387': 'floated_cross',
                   '388': 'jumping',
                   '389': 'goalkeeper_sliding',
                   '390': 'player_id_causing_penalty',
                   '391': 'shot_mishit',
                   '392': 'foul_reckless_offence',
                   '393': 'foul_tactical',
                   '394': 'corner_not_taken',
                   '395': 'goalkeeper_x_coordinate_at_time_of_goal',
                   '396': 'goalkeeper_y_coordinate_at_time_of_goal',
                   '397': 'blocked_clearance',
                   '398': 'foul_goalkeeper_challenge',
                   '399': 'foul_intended_tackle_target',
                   # 400 - 405: no qualifier
                   '406': 'data_collection_complete',
                   # 407 - 435: no qualifier
                   '436': 'var_pre_review_event_type',
                   # 437 - 457: no qualifier
                   '458': 'not_assisted',
                   '459': 'event_type_review',
                   # 460 - 463: no qualifier
                   '464': 'take_on_space',
                   '465': 'take_on_overtake',
                   # 466: no qualifier
                   '467': 'defensive_1_v_1',
                   '468': 'related_error_id',
                   # 469 - 471: no qualifier
                   '472': 'fantasy_assist_id',
                   }