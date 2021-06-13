# Changelog

This project sticks to [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).

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
