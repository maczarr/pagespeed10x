# Changelog

This project sticks to [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).

## 2021-05-31 - unreleased

- Fix: If CrUX data isn't from the actual URL but only provided from the
  origin (`origin_fallback` is true) it will be treated as if there is no
  CrUX data.
  Reason for this decision: After saving the data from the API a difference
  between actual CrUX data for the URL and fallback data can't be determined
  any longer. If someone requests performance data for a specific URL I don't
  see why a fallback to origin data would be of interest.

## 2021-04-25 - 1.0.0

- Initial release.
