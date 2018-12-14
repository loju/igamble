# igamble

Simple gaming platform written in Django 2.1
User can create account by himself.

Each user login is awarded by configurable amount of money (Admin -> Bonus for login models)
Each deposit is awarded in similar way (Admin -> Bonus for deposit models) - threshold is used.

User can use spin button as simulation of game and randomly win/lost configurable money 
(could be configured by setting file - BET_VALUE)

We have two types of wallets: real and bonus.
Real wallet always has prority (if there are some money), then bonus wallet could be used.

We can transfer money from bonus wallet to real (oldest wallet has priority in both cases) when:
factor * last deposit < spent money from  current real wallet

Factor could be defined in (Admin -> Wager models)
  