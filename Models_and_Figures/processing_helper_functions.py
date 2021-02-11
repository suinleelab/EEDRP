def final_processing(encode_method, years_data, only_one, feature_set, feature_names, ALL_FEATURES_TIME):
    import h5py
    import pandas as pd
    

    #with h5py.File("../DATA/PROCESSED/standardized_demographics_stacked_imputed/2yrprev_within3.h5", 'r') as hf:
    #    ALL_FEATURES_TIME = hf["features"][:]
    
    simplify_apoe = True
    years = 2
    
    demographic_cols_allyears = ['dcfdx__1.0','dcfdx__2.0', 'dcfdx__3.0', 'med_con_sum_cum', 
                                 'vasc_3dis_sum', 'vasc_risks_sum', 'hypertension_cum', 
                                 'cancer_cum', 'diabetes_sr_rx', 'dm_cum', 'headinjrloc_cum', 
                                 'thyroid_cum', 'claudication_cum', 'heart_cum', 'stroke_cum']
    demographic_cols_oneyear = ['apoe_genotype__22.0', 'apoe_genotype__23.0', 'apoe_genotype__24.0', 
                                'apoe_genotype__33.0', 'apoe_genotype__34.0', 'apoe_genotype__44.0', 
                                'race__1.0', 'race__2.0', 'race__3.0', 'race__6.0', 'age_at_visit', 
                                'educ', 'msex', 'spanish']
    
    feature_set_dict = {}
    feature_set_dict['baseline_demographics_cols'] = ['age_at_visit', 'educ', 'msex', 
                                                      'apoe_genotype__22.0', 'apoe_genotype__23.0', 
                                                      'apoe_genotype__24.0', 'apoe_genotype__33.0', 
                                                      'apoe_genotype__34.0', 'apoe_genotype__44.0']
    feature_set_dict['baseline_demographics_withmci_cols'] = ['age_at_visit', 'educ', 'msex', 
                                                              'apoe_genotype__22.0', 'apoe_genotype__23.0',
                                                              'apoe_genotype__24.0', 'apoe_genotype__33.0',
                                                              'apoe_genotype__34.0', 'apoe_genotype__44.0',
                                                              'dcfdx__2.0', 'dcfdx__3.0']
    feature_set_dict['baseline_mci_cols'] = ['dcfdx__2.0', 'dcfdx__3.0']
    feature_set_dict['baseline_mmse30_cols'] = ['age_at_visit', 'educ', 'msex', 
                                                'apoe_genotype__22.0', 'apoe_genotype__23.0', 
                                                'apoe_genotype__24.0', 'apoe_genotype__33.0', 
                                                'apoe_genotype__34.0', 'apoe_genotype__44.0', 'cts_mmse30']
    feature_set_dict['baseline_linear_selected_features'] = ['age_at_visit', 'educ', 'msex', 'apoe_genotype__22.0', 
                                                             'apoe_genotype__23.0', 'apoe_genotype__24.0', 
                                                             'apoe_genotype__33.0', 'apoe_genotype__34.0', 
                                                             'apoe_genotype__44.0', 'cts_df', 'cts_doperf', 
                                                             'cts_ebmt', 'cts_db','cts_ebdr']
    feature_set_dict['simplified_cols_withapoe'] = ['age_at_visit', 'educ', 'msex', 'apoe_genotype__22.0', 
                                                    'apoe_genotype__23.0', 'apoe_genotype__24.0',
                                                    'apoe_genotype__33.0', 'apoe_genotype__34.0', 
                                                    'apoe_genotype__44.0', 'cts_catflu', 'cts_mmse30', 
                                                    'cts_sdmt', 'cts_wli', 'cts_wlii', 'cts_wliii']
    feature_set_dict['simplified_cols_withoutapoe'] = ['age_at_visit', 'educ', 'msex', 'cts_catflu', 'cts_mmse30', 
                                                       'cts_sdmt', 'cts_wli', 'cts_wlii', 'cts_wliii']
    feature_set_dict['all_cols'] = ['age_at_visit', 'educ', 'msex', 'apoe_genotype__22.0', 
                                       'apoe_genotype__23.0', 'apoe_genotype__24.0', 
                                       'apoe_genotype__33.0', 'apoe_genotype__34.0', 
                                       'apoe_genotype__44.0', 'spanish', 'race__1.0', 
                                       'race__2.0', 'race__3.0', 'race__6.0', 'dcfdx__1.0', 
                                       'dcfdx__2.0',  'dcfdx__3.0', 'med_con_sum_cum', 
                                       'vasc_3dis_sum', 'vasc_risks_sum', 'hypertension_cum', 
                                       'cancer_cum', 'diabetes_sr_rx', 'dm_cum', 'headinjrloc_cum', 
                                       'thyroid_cum', 'claudication_cum', 'heart_cum', 'stroke_cum', 
                                       'cts_animals', 'cts_bname', 'cts_catflu', 'cts_db', 
                                       'cts_delay', 'cts_df', 'cts_doperf', 'cts_ebdr', 'cts_ebmt', 
                                       'cts_fruits', 'cts_idea', 'cts_lopair', 'cts_mmse30', 
                                       'cts_nccrtd', 'cts_pmat', 'cts_pmsub', 'cts_read_nart', 
                                       'cts_sdmt', 'cts_story', 'cts_stroop_cname', 
                                       'cts_stroop_wread', 'cts_wli', 'cts_wlii', 'cts_wliii']
    feature_set_dict['cumulative_cols'] = ['age_at_visit', 'educ', 'msex', 'apoe_genotype__22.0', 
                                           'apoe_genotype__23.0', 'apoe_genotype__24.0', 
                                           'apoe_genotype__33.0', 'apoe_genotype__34.0', 
                                           'apoe_genotype__44.0', 'spanish', 'race__1.0', 
                                           'race__2.0', 'race__3.0', 'race__6.0', 'dcfdx__1.0', 
                                           'dcfdx__2.0',  'dcfdx__3.0', 'med_con_sum_cum', 
                                           'vasc_3dis_sum', 'vasc_risks_sum', 'hypertension_cum', 
                                           'cancer_cum', 'diabetes_sr_rx', 'dm_cum', 'headinjrloc_cum', 
                                           'thyroid_cum', 'claudication_cum', 'heart_cum', 'stroke_cum',
                                           'cts_animals', 'cts_bname', 'cts_catflu', 'cts_db', 
                                           'cts_delay', 'cts_df', 'cts_doperf', 'cts_ebdr', 'cts_ebmt', 
                                           'cts_fruits', 'cts_idea', 'cts_lopair', 'cts_mmse30', 
                                           'cts_nccrtd', 'cts_pmat', 'cts_pmsub', 'cts_read_nart', 
                                           'cts_sdmt', 'cts_story', 'cts_stroop_cname', 'cts_stroop_wread', 
                                           'cts_wli', 'cts_wlii', 'cts_wliii', 'cogn_ep', 'cogn_po', 
                                           'cogn_ps', 'cogn_se', 'cogn_wo', 'cogn_global']
    

    # Change depending on which test you want to run
    cols_to_use = feature_set_dict[feature_set]
    cols_name = feature_set

    demographic_cols = []
    for col in demographic_cols_oneyear:
        if col in cols_to_use:
            demographic_cols.append(col)


    for col in demographic_cols_allyears:
        if col in cols_to_use:
            if not only_one:
                for i in range(years_data+1):
                    demographic_cols.append(col+'_'+str(i)+'yearsago')
            else:
                demographic_cols.append(col)

    demographics = pd.DataFrame(columns=demographic_cols)

    index_allyears = []
    index_oneyear = []
    for i in range(len(feature_names)):
        if feature_names[i] in cols_to_use:
            if feature_names[i] in demographic_cols_allyears:
                index_allyears.append(i)
            elif feature_names[i] in demographic_cols_oneyear:
                index_oneyear.append(i)

    for i in range(ALL_FEATURES_TIME.shape[0]):
        demographics = demographics.append(pd.Series(index=demographic_cols), ignore_index=True)
        for j in index_oneyear:
            if not only_one:
                demographics.iloc[i][feature_names[j]] = ALL_FEATURES_TIME[i][years][j]
            else:
                demographics.iloc[i][feature_names[j]] = ALL_FEATURES_TIME[i][years][j]
        for j in index_allyears:
            if not only_one:
                for k in range(years_data+1):
                    demographics.iloc[i][(feature_names[j]+'_'+str(k)+'yearsago')] = ALL_FEATURES_TIME[i][years-k][j]
            else:
                demographics.iloc[i][(feature_names[j])] = ALL_FEATURES_TIME[i][years-years_data][j]

    if simplify_apoe and ('apoe_genotype__44.0' in cols_to_use):
        apoe_cols = ['apoe_genotype__22.0', 'apoe_genotype__23.0', 'apoe_genotype__24.0', 'apoe_genotype__33.0', 'apoe_genotype__34.0']
        demographics['apoe4_1copy'] = demographics['apoe_genotype__24.0'] + demographics['apoe_genotype__34.0']
        demographics.rename(columns={'apoe_genotype__44.0': 'apoe4_2copies'}, inplace=True)
        demographics.drop(labels=apoe_cols, axis=1, inplace=True)

    if cols_name in ['baseline_mci_cols', 'baseline_demographics_withmci_cols']:
        if not only_one:
            for i in range(years_data+1):
                demographics['mci_'+str(i)+'yearsago'] = demographics['dcfdx__2.0_'+str(i)+'yearsago'] + demographics['dcfdx__3.0_'+str(i)+'yearsago']
                demographics.drop(labels=['dcfdx__2.0_'+str(i)+'yearsago', 'dcfdx__3.0_'+str(i)+'yearsago'], axis=1, inplace=True)
        else:
            demographics['mci'] = demographics['dcfdx__2.0'] + demographics['dcfdx__3.0']
            demographics.drop(labels=['dcfdx__2.0', 'dcfdx__3.0'], axis=1, inplace=True)

    for col in demographics.columns.values:
        demographics[col] = pd.to_numeric(demographics[col])
        
    constructed_data = demographics.copy()
    half_life = 3

    for i in range(ALL_FEATURES_TIME.shape[0]):
        patient = pd.DataFrame(ALL_FEATURES_TIME[i])
        patient.columns = feature_names
        drop_cols = set([x for x in feature_set_dict['cumulative_cols'] if x not in cols_to_use])
        for col in demographic_cols_allyears:
            drop_cols.add(col)
        for col in demographic_cols_oneyear:
            drop_cols.add(col)
        patient.drop(labels=drop_cols, axis=1, inplace=True)

        for j in patient.columns.values:
            if not only_one:
                constructed_data.at[i,str(j)+"_0yearsago"] = patient.iloc[years][j]
                if encode_method != "current_only":
                    if encode_method=='sma':
                        constructed_data.at[i,str(j)+'_sma'] = patient[j].rolling(years_data+1).mean()[years_data]
                    elif encode_method=='ema':
                        constructed_data.at[i,str(j)+'_ema'+str(half_life)] = patient[j].ewm(halflife=half_life, adjust=False).mean()[years_data]
                    elif encode_method=='all_ma':
                        constructed_data.at[i,str(j)+'_sma'] = patient[j].rolling(years_data+1).mean()[years_data]
                        constructed_data.at[i,str(j)+'_ema1'] = patient[j].ewm(halflife=1, adjust=False).mean()[years_data]
                        constructed_data.at[i,str(j)+'_ema2'] = patient[j].ewm(halflife=2, adjust=False).mean()[years_data]
                        constructed_data.at[i,str(j)+'_ema3'] = patient[j].ewm(halflife=3, adjust=False).mean()[years_data]
                    elif encode_method=='slopes':
                        constructed_data.at[i,str(j)+'_overalltrajectory'] = (patient.iloc[0][j]-patient.iloc[years_data][j])/(years_data)
                        for k in range(0,years_data):
                            constructed_data.at[i,str(j)+'_yr'+str(k+1)+'to'+str(k)+'trajectory'] = patient.iloc[years-(k+1)][j]-patient.iloc[years-k][j]
                        for k in range(1,years_data+1):
                            constructed_data.at[i,str(j)+'_'+str(k)+'yearsago'] = patient.iloc[years-k][j]
                    else:
                        for k in range(1,years_data+1):
                            constructed_data.at[i,str(j)+'_'+str(k)+'yearsago'] = patient.iloc[years-k][j]
            else:
                if encode_method != "current_only":
                    if encode_method=='sma':
                        constructed_data.at[i,str(j)+'_sma'] = patient[j].rolling(years_data+1).mean()[years_data]
                    elif encode_method=='ema':
                        constructed_data.at[i,str(j)+'_ema'+str(half_life)] = patient[j].ewm(halflife=half_life, adjust=False).mean()[years_data]
                    elif encode_method=='all_ma':
                        constructed_data.at[i,str(j)+'_sma'] = patient[j].rolling(years_data+1).mean()[years_data]
                        constructed_data.at[i,str(j)+'_ema1'] = patient[j].ewm(halflife=1, adjust=False).mean()[years_data]
                        constructed_data.at[i,str(j)+'_ema2'] = patient[j].ewm(halflife=2, adjust=False).mean()[years_data]
                        constructed_data.at[i,str(j)+'_ema3'] = patient[j].ewm(halflife=3, adjust=False).mean()[years_data]
                    else:
                        constructed_data.at[i,str(j)] = patient.iloc[years-years_data][j]
    return constructed_data


def unstandardize(zscores, m, s):
    return zscores*s + m


def unstandardize_data(data_matrix):
    import pandas as pd
    
    unnorm_data_matrix = data_matrix.copy()
    dset = '2yrprev_within3'
    meanstds =  pd.read_csv("../DATA/PROCESSED/standardized/%s_mean_std.csv"%dset,index_col=0)

    for i in unnorm_data_matrix.columns.values:
        lookup_col = i
        if i[-8:]=='yearsago':
            lookup_col = i[:-10]
        try:
            unnorm_data_matrix[i] = unstandardize(unnorm_data_matrix[i], meanstds.loc[lookup_col][" mean"], meanstds.loc[lookup_col][" std"])
        except:
            continue
    
    return unnorm_data_matrix


def normalize_names(data_matrix):
    feature_names_dict = {'educ': 'Years of Education',
                          'age_at_visit': 'Age',
                          'msex': 'Sex: Male',
                          'apoe4_1copy': 'Has 1 copy of APOE e4 allele',
                          'apoe4_2copies': 'Has 2 copies of APOE e4 allele',
                          'cts_catflu': 'Categorical Fluency',
                          'cts_sdmt': 'Symbol Digital Modality Test',
                          'cts_wli': 'Word List Immediate Recall',
                          'cts_wlii': 'Word List Delayed Recall',
                          'cts_wliii': 'Word List Recognition',
                          'dcfdx__1.0': 'No Cognitive Impairment Diagnosis',
                          'dcfdx__2.0': 'Mild Cognitive Impairment Diagnosis',
                          'cts_mmse30': 'Mini-Mental State Exam',
                          'cts_fruits': 'Categorical Fluency: Fruits',
                          'cts_delay': 'Logical Memory II Delayed',
                          'cts_bname': 'Boston Naming',
                          'cts_story': 'Logical Memory I Immediate',
                          'cts_lopair': 'Line Orientation',
                          'cts_ebmt': 'East Boston Immediate Recall',
                          'cts_ebdr': 'East Boston Delayed Recall',
                          'cts_animals': 'Categorical Fluency: Animals',
                          'cts_stroop_cname': 'Stroop Color Naming',
                          'cts_nccrtd': 'Number Comparison',
                          'cts_pmat': 'Progressive Matrices',
                          'cts_pmsub': 'Progressive Matrices Subset',
                          'diabetes_sr_rx': 'Has diabetes or has taken diabetes medication',
                          'cts_catflu_0yearsago': 'Categorical Fluency at t',
                          'cts_sdmt_0yearsago': 'Symbol Digital Modality Test at t',
                          'cts_wli_0yearsago': 'Word List Immediate Recall at t',
                          'cts_wlii_0yearsago': 'Word List Delayed Recall at t',
                          'cts_wliii_0yearsago': 'Word List Recognition at t',
                          'dcfdx__1.0_0yearsago': 'No Cognitive Impairment Diagnosis at t',
                          'dcfdx__2.0_0yearsago': 'Mild Cognitive Impairment Diagnosis at t',
                          'cts_mmse30_0yearsago': 'Mini-Mental State Exam at t',
                          'cts_fruits_0yearsago': 'Categorical Fluency: Fruits at t',
                          'cts_delay_0yearsago': 'Logical Memory II Delayed at t',
                          'cts_bname_0yearsago': 'Boston Naming at t',
                          'cts_story_0yearsago': 'Logical Memory I Immediate at t',
                          'cts_lopair_0yearsago': 'Line Orientation at t',
                          'cts_ebmt_0yearsago': 'East Boston Immediate Recall at t',
                          'cts_animals_0yearsago': 'Categorical Fluency: Animals at t',
                          'cts_stroop_cname_0yearsago': 'Stroop Color Naming at t',
                          'cts_nccrtd_0yearsago': 'Number Comparison at t',
                          'cts_pmat_0yearsago': 'Progressive Matrices at t',
                          'cts_pmsub_0yearsago': 'Progressive Matrices Subset at t',
                          'diabetes_sr_rx_0yearsago': 'Has diabetes or has taken diabetes medication at t',
                          'cts_catflu_1yearsago': 'Categorical Fluency at t-1',
                          'cts_sdmt_1yearsago': 'Symbol Digital Modality Test at t-1',
                          'cts_wli_1yearsago': 'Word List Immediate Recall at t-1',
                          'cts_wlii_1yearsago': 'Word List Delayed Recall at t-1',
                          'cts_wliii_1yearsago': 'Word List Recognition at t-1',
                          'dcfdx__1.0_1yearsago': 'No Cognitive Impairment Diagnosis at t-1',
                          'dcfdx__2.0_1yearsago': 'Mild Cognitive Impairment Diagnosis at t-1',
                          'cts_mmse30_1yearsago': 'Mini-Mental State Exam at t-1',
                          'cts_fruits_1yearsago': 'Categorical Fluency: Fruits at t-1',
                          'cts_delay_1yearsago': 'Logical Memory II Delayed at t-1',
                          'cts_bname_1yearsago': 'Boston Naming at t-1',
                          'cts_story_1yearsago': 'Logical Memory I Immediate at t-1',
                          'cts_lopair_1yearsago': 'Line Orientation at t-1',
                          'cts_ebmt_1yearsago': 'East Boston Immediate Recall at t-1',
                          'cts_ebdr_1yearsago': 'East Boston Delayed Recall at t-1',
                          'cts_animals_1yearsago': 'Categorical Fluency: Animals at t-1',
                          'cts_stroop_cname_1yearsago': 'Stroop Color Naming at t-1',
                          'cts_nccrtd_1yearsago': 'Number Comparison at t-1',
                          'cts_pmat_1yearsago': 'Progressive Matrices at t-1',
                          'cts_pmsub_1yearsago': 'Progressive Matrices Subset at t-1',
                          'diabetes_sr_rx_1yearsago': 'Has diabetes or has taken diabetes medication at t-1',
                          'cts_catflu_2yearsago': 'Categorical Fluency at t-2',
                          'cts_sdmt_2yearsago': 'Symbol Digital Modality Test at t-2',
                          'cts_wli_2yearsago': 'Word List Immediate Recall at t-2',
                          'cts_wlii_2yearsago': 'Word List Delayed Recall at t-2',
                          'cts_wliii_2yearsago': 'Word List Recognition at t-2',
                          'dcfdx__1.0_2yearsago': 'No Cognitive Impairment Diagnosis at t-2',
                          'dcfdx__2.0_2yearsago': 'Mild Cognitive Impairment Diagnosis at t-2',
                          'cts_mmse30_2yearsago': 'Mini-Mental State Exam at t-2',
                          'cts_fruits_2yearsago': 'Categorical Fluency: Fruits at t-2',
                          'cts_delay_2yearsago': 'Logical Memory II Delayed at t-2',
                          'cts_bname_2yearsago': 'Boston Naming at t-2',
                          'cts_story_2yearsago': 'Logical Memory I Immediate at t-2',
                          'cts_lopair_2yearsago': 'Line Orientation at t-2',
                          'cts_ebmt_2yearsago': 'East Boston Immediate Recall at t-2',
                          'cts_ebdr_2yearsago': 'East Boston Delayed Recall at t-2',
                          'cts_animals_2yearsago': 'Categorical Fluency: Animals at t-2',
                          'cts_stroop_cname_2yearsago': 'Stroop Color Naming at t-2',
                          'cts_nccrtd_2yearsago': 'Number Comparison at t-2',
                          'cts_pmat_2yearsago': 'Progressive Matrices at t-2',
                          'cts_pmsub_2yearsago': 'Progressive Matrices Subset at t-2',
                          'diabetes_sr_rx_2yearsago': 'Has diabetes or has taken diabetes medication at t-2'}

    norm_feature_names = []
    for feat_name in data_matrix.columns.values:
        try:
            new_name = feature_names_dict[feat_name]
        except:
            new_name = feat_name
        norm_feature_names.append(new_name)
        
    return norm_feature_names