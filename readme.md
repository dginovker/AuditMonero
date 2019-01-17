# Audit Monero

Monero is a privacy focused cryptocurrency, and as such is speculated to be inauditable. This project aims to disprove this, with proof of concept audits for the Monero blockchain.

Ways coins can come into existence:
- Coinbase mints (mining reward)
- Transactions

Transactions can be further broken down into 3 categories:
- Pre-RingCT
- RingCT
- RingCT + Bulletproofs

Additionally, there are 3 versions of the Monero blockchain, each coming out at a different fork date. Below is a table of which permutations have been tested and verified.

Blockchain Version | Coinbase Mints | Pre-RingCT | RingCT | RingCT + Bulletproofs
:--|:--|:--|:--|:--
Version 1 |
Version 2 |
Version 3 | [Verified](https://raw.githubusercontent.com/dginovker/AuditMonero/master/venv/CoinbaseMints.csv) |
