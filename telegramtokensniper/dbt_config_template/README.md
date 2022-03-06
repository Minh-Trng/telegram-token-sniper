this project uses https://github.com/Minh-Trng/dex-buy-tools for performing buys.
Note that the TelegramTokenSniper requires a separate 'buy_params_template.yml' and 'wallet_data.yml' for each chain. The file name has to 
be prefixed with the abbreviation of the corresponding chain, e.g. 'avax_buy_params.yml' and "avax_wallet_data.yml". 
the abbreviations for the chains currently used: [avax, bsc, eth, ftm, poly]

if you dont want to perform buys on a certain chain, dont provide the private key in the wallet-files (the files need to exist though, else the program might crash)

the 'template'-suffix has to be removed from the files as well as the 'dbt_config_template'-directory

to visualize:


![grafik](https://user-images.githubusercontent.com/46103853/156925750-0509fde4-2236-4f13-8565-2f8612968b85.png)
