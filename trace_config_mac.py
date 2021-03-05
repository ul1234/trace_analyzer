#!/usr/bin/python
# -*- coding: utf-8 -*-

# color: 'k', 'grey', 'brown', 'darkred', 'r', 'orange', 'gold', 'y', 'yellowgreen', 'g', 'lime', springgreen', 'c', 'darkcyan',
#       'skyblue', 'steelblue', 'navy', 'b', 'violet', 'purple', 'm', 'pink', 'deeppink'
# component: [(priority, [(id, color, {'same_core': False, 'show': False, 'xtick': True}), ...]), ...]
TRACES_CONFIG = {
    'DL SRP': [(10, 'DlSrp FFT', [(('NR_L0_DLSRP_DL_FFT_DATA_START', 'NR_L0_DLSRP_DL_FFT_DATA_END'), 'r', {'show': False})]),
               (11, 'DlSrp Pdcch', [(('NR_L0_DLSRP_PDCCH_START', 'NR_L0_DLSRP_PDCCH_END'), 'm', {'xtick': True})]),
              ],
    'PDCCH': [(20, 'Pdcch Brp', [(('NR_L0_DLC_PDCCH_BRP_START', 'NR_L0_DLC_PDCCH_BRP_SD_END'), 'k', {})]),
              (23, 'MSG to L1', [('FRAMEWORK_MSG_SEND', 'g', {'filter': 'NR_L0L1_PHY_DLC_UL_SCH_DATA_READY_IND', 'combine_core': True, 'rand_core_color': True}),
                                 ('FRAMEWORK_MSG_SEND', 'b', {'filter': 'NR_L0L1_PHY_DLC_PDSCH_CTRL_IND', 'combine_core': True, 'rand_core_color': True}),
                                 ('FRAMEWORK_MSG_SEND', 'm', {'filter': 'NR_L0L1_PHY_BRP_PDSCH_DATA_IND', 'combine_core': True, 'rand_core_color': True})]),
             ],
    'PDSCH BRP': [(35, 'HARQ Msg', [('FRAMEWORK_MSG_SEND', 'r', {'filter': 'NR_L0_ULC_DLC_SEND_HARQ_IND'})]),
                 ],
    'UL CTRL': [(40, 'UlCtrl Tti', [(('NR_L0_ULC_SCHEDULE_TTI_START', 'NR_L0_ULC_SCHEDULE_TTI_END'), 'c', {'show': False})]),
               ],
    'MAC': [(80, 'L1 UL PHY', [(('NR_UL_L1_RX_PDCCH_PHY_IND_START', 'NR_UL_L1_RX_PDCCH_PHY_IND_END'), 'r', {})]),
            (81, 'L1 DL PHY', [('NR_L1_PHY_PDSCH_CTRL_IND', 'g', {})]),
           ]
              }

