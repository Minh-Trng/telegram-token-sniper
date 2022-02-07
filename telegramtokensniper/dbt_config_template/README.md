this project uses https://github.com/Minh-Trng/dex-buy-tools for performing buys.
Note that the TelegramTokenSniper requires a separate 'buy_params_template.yml' and 'wallet_data.yml' for each chain. The file name has to 
be prefixed with the abbreviation of the corresponding chain, e.g. 'avax_buy_params.yml' and "avax_wallet_data.yml". 
the abbreviations for the chains currently used: [avax, bsc, eth, ftm, poly]

the 'template'-suffix has to be removed from the files as well as the 'dbt_config_template'-directory