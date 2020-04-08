# Sepulsa Client 
[![Build Status](https://github.com/vousmeevoyez/sepulsa/workflows/Python%20Pipeline/badge.svg)](https://github.com/vousmeevoyez/sepulsa/workflows/Python%20Pipeline/badge.svg)
[![codecov](https://codecov.io/gh/vousmeevoyez/sepulsa/branch/master/graph/badge.svg)](https://codecov.io/gh/vousmeevoyez/sepulsa)
[![Stable Version](https://img.shields.io/github/v/tag/vousmeevoyez/sepulsa)](https://img.shields.io/github/v/tag/vousmeevoyez/sepulsa)
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE.md)

Unofficial Sepulsa Client using Python 

**This library allows you to quickly and easily use the Sepulsa v3 via Python.**
List of implemented API:
* Pulsa Prabayar
* Pulsa Pascabayar
* Paket Data
* PLN Prabayar
* PLN Pascabayar
* BPJS Kesehatan
* PDAM
* Telkom

reference: https://horven.sumpahpalapa.com/swagger/kraken/index.html#!/

# Table of Contents

* [Installation](#installation)
* [Quick Start](#quick-start)


### Installation
```
pip3 install sepulsa
```
### Quick Start
```
from sepulsa import build_client

# get balance
sepulsa = build_client("https://horven-api.sumpahpalapa.com/api", "username", "api-key")
sepulsa.get_products()
```
more example checkout:
- [Example Code](https://github.com/vousmeevoyez/sepulsa/tree/master/examples)


## Built With

* [Requests](https://requests.readthedocs.io/en/master/) - HTTP Library Used

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Kelvin Desman** - [Vousmeevoyez](https://github.com/vousmeevoyez/)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
