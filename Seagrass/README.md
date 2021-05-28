Seagrass is monitored anually by the Washington State Department of Natural Resources (DNR). WA-DNR has produced this [map](https://www.arcgis.com/apps/webappviewer/index.html?id=83b8389234454abc8725827b49272a31) which is very helpful. Seagrass is a key indicator of ecosystem health as it serves as food source, nursery and shelter for many different species, including juvenile salmon. For more information I recommend reading [Eelgrass as Valuable Nearshore Foraging Habitat for Juvenile Pacific Salmon in the Early Marine Period](https://dspace.library.uvic.ca/handle/1828/7683) by Laura Kennedy, University of Victoria. This data is a small subset of what is published by WA-DNR, the whole dataset is available [here](https://data-wadnr.opendata.arcgis.com/search?groupIds=6156be63723248acb386917641ff397f&q=puget%20sound%20seagrass%20monitoring%20complete%20download). This dataset includes the location of the sample, the time the sample was started, and information about seagrass levels at the sample. This is constructed from several different tables in the original dataset (site_info, site_samples, and site_results).

This chart explains the seagrass data obtained from the 'results' table

![Seagrass Variable Dictionary](https://raw.githubusercontent.com/OscarLewis/salmon-fishing/main/Seagrass/results_table.png)

The 'SeagrassSites.gpkg' file only has a single layer of Seagrass observations from WA-DRN. This layer contains the following attributes:

- site_code: A sample site identifier used internally.
- samp_status_disp: The status of the sample, pretty much all data will be of type 'sampled'.
- veg_class: The seagrass species present at the site, summarized from all available site visits.
  - Domain:
    - no_data = the site has not been sampled.
    - no_grass = no seagrass was observed at the site.
    - Zm = Eelgrass.
    - Phyllo = Surfgrass.
    - Zj = Z. japonica.
    - Zm_Zj = Eelgrass and Z. japonica mix.
    - Zm_Phyllo = Eelgrass and Surfgrass mix.
- long_term_trend: Classification of the site with respect to the long-term trend in native seagrass over time.
  - Domain:
    - increase = native seagrass abundance has increased.
    - decline = native seagrass abundance has declined.
    - no_trend = no evidence of trend in native seagrass abundance.
    - no_data = the site has not been sampled.
    - limited_data = the site has been sampled but there is insufficient data to make a trend assessment
    - no_grass = no seagrass was observed at the site.
    - trace = native seagrass observed but only at trace quantities that were insufficient to make a trend assessment.
    - obstructed = the site was visited but not sampled due to obstruction. Trend was not assessed.
    - not classified (nonDNR data) = only data from external organization
      available, not assessed for trend.
- recent_6yr_trend: Classification of the site with respect to the recent (6 year) trend in native seagrass over time. Has the same domain as long_term_trend
- veg_code: Code for vegetation type represented in the transect result. Only “nativesg” is used in this database
- veg_frac: Estimated vegetated fraction
- samp_area_ft2: Eelgrass (sample) polygon area in square feet
- veg_area_ft2: Estimated vegetation area in square feet
- veg_area_se_ft2: Estimated standard error of estimate of vegetation area in square feet
- veg_mind_mean_ft: Estimate of mean minimum depth of vegetation in feet (MLLW)
- veg_mind_deepest_ft: Deepest observed value for minimum depth of vegetation in feet (MLLW)
- veg_mind_shallowest_ft: Shallowest observed value for minimum depth of vegetation in feet (MLLW)
- veg_mind_se_ft: Estimated standard error of estimate of mean minimum depth in feet
- veg_maxd_mean_ft: Estimate of mean maximum depth of vegetation in feet (MLLW)
- veg_maxd_deepest_ft: e Deepest value for maximum depth of vegetation observed in feet (MLLW)
- veg_maxd_shallowest_ft: Shallowest value for maximum depth of vegetation observed in feet (MLLW)
- date_samp_start: The date at which surveying is initiated for a site sample
- year: The year in wich surveying is initiated for a site
