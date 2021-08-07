# Changelog

This project sticks to [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).

## Unreleased

- Upgrade Influxdb-Docker-Container from 2.0.4 to 2.0.7
- Upgrade Grafana-Docker-Container from 7.5.4 to 8.1.0
- Fix: Added the missing notifiers- and plugins-folders to the grafana provisioning config folder structure.

## 2021-08-07 - 1.1.0

- Updated Grafana Dashboard.
  - Legend
    - Legend has a more human readable format.
    - It doesn't repeat the URL anymore, because it has already been selected in the drop down and it can be very long.
    - Fix: The proportions on Field-Data are preconfigured to use the right Y-axis (so this known issue is gone now).
    - On Lab-Data the average value for the choosen time range is shown.
  - Fix: On Field-Data showing the Lighthouse version was incorrect as this data isn't collected by Lighthouse.
  - Field-Data has now three gauges at the top showing the latest value for the core web vitals.
  - Thresholds in Lab-Data have been adjusted to meet the current Lighthouse v8 thresholds. The dashboard will always show the mobile thresholds even if you choose "Desktop" in the drop down because – as far as I know – Grafana doesn't have a concept of "dynamic" thresholds.
  - Updated Screenshots.

## 2021-06-13 - 1.0.2

- As of June 10th 2021 any metric in crux data (loadingExperience) can be
  provided if it meets the threshold of data ([PSI Release Notes](https://developers.google.com/speed/docs/insights/release_notes)). Before there was crux data or not, but
  now there my be only some metrics. The code is now adjusted to meet this
  behaviour.

## 2021-05-31 - 1.0.1

- Fix: If CrUX data isn't from the actual URL but only provided from the
  origin (`origin_fallback` is true) it will be treated as if there is no
  CrUX data.
  Reason for this decision: After saving the data from the API a difference
  between actual CrUX data for the URL and fallback data can't be determined
  any longer. If someone requests performance data for a specific URL I don't
  see why a fallback to origin data would be of interest.

## 2021-04-25 - 1.0.0

- Initial release.
