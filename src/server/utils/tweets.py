from tweetparser import *
tweets = [(u'Wed May 23 20:38:32 +0000 2018', u'RT @DaveSimonoff: $BTC reached my second target at 8.6k (thanks to #Tether) and retraced back to the previous support line of 7.8-7.9k. Nex\u2026'), (u'Wed May 23 20:06:11 +0000 2018', u'RT @ProducToken: The MORE you INVEST, the HIGHER is your BONUS ! \nUP to 35% \U0001f4b0\U0001f4b0\U0001f4b0\nINVEST NOW -&gt; https://t.co/4So9Aym8Gn    \n\n#crypto #tokensa\u2026'), (u'Wed May 23 19:46:10 +0000 2018', u'RT @ProducToken: The MORE you INVEST, the HIGHER is your BONUS ! \nUP to 35% \U0001f4b0\U0001f4b0\U0001f4b0\nINVEST NOW -&gt; https://t.co/4So9Aym8Gn    \n\n#crypto #tokensa\u2026'), (u'Wed May 23 19:38:00 +0000 2018', u'RT @KingCrypto_: Ready to begin trading cryptocurrency? Then you should definitely check out Coinigy...\n\nGet a 30 day free trial when you s\u2026'), (u'Wed May 23 19:26:10 +0000 2018', u"RT @RealCryptoLion: Lots of FEAR in the crypto space right now. Don't be an idiot and sell your coins, because you will end up buying them\u2026"), (u'Wed May 23 19:11:44 +0000 2018', u'#XDCE on #GetBTC #Exchange. Start #trading with #XDCE against #BTC on @ExchangeGetBTC \n\n#cryptocurrency #XinFin\u2026 https://t.co/MYnHbVvq8t'), (u'Wed May 23 18:58:42 +0000 2018', u'RT @ProducToken: The MORE you INVEST, the HIGHER is your BONUS ! \nUP to 35% \U0001f4b0\U0001f4b0\U0001f4b0\nINVEST NOW -&gt; https://t.co/4So9Aym8Gn    \n\n#crypto #tokensa\u2026'), (u'Wed May 23 18:31:50 +0000 2018', u"RT @RealCryptoLion: Lots of FEAR in the crypto space right now. Don't be an idiot and sell your coins, because you will end up buying them\u2026"), (u'Wed May 23 18:30:01 +0000 2018', u"RT @KingCrypto_: Want to trade altcoins? I'd recommend using Binance to get started...\n\n\U0001f449https://t.co/EQZfX0xBCJ\n\n#cryptocurrency #bitcoin\u2026"), (u'Wed May 23 18:14:18 +0000 2018', u'RT @ProducToken: The MORE you INVEST, the HIGHER is your BONUS ! \nUP to 35% \U0001f4b0\U0001f4b0\U0001f4b0\nINVEST NOW -&gt; https://t.co/4So9Aym8Gn    \n\n#crypto #tokensa\u2026'), (u'Wed May 23 17:55:35 +0000 2018', u"RT @RealCryptoLion: Lots of FEAR in the crypto space right now. Don't be an idiot and sell your coins, because you will end up buying them\u2026"), (u'Wed May 23 17:19:32 +0000 2018', u"RT @RealCryptoLion: Lots of FEAR in the crypto space right now. Don't be an idiot and sell your coins, because you will end up buying them\u2026"), (u'Wed May 23 17:11:10 +0000 2018', u"RT @RealCryptoLion: Lots of FEAR in the crypto space right now. Don't be an idiot and sell your coins, because you will end up buying them\u2026"), (u'Wed May 23 16:56:56 +0000 2018', u'Market Cap: $332.032.466.273 - 24h Vol: $19.512.519.815 - BTC Dominance: 39.3% #btc #bitcoin #altcoins\u2026 https://t.co/Qvlqwt5SG0'), (u'Wed May 23 16:43:53 +0000 2018', u"Lots of FEAR in the crypto space right now. Don't be an idiot and sell your coins, because you will end up buying t\u2026 https://t.co/kt5EjBSAA4"), (u'Wed May 23 16:30:18 +0000 2018', u'The World Crypto Markets = RED\nLast Major World Event = WEDDING\n\nGame of Thrones had it right\n\n#tenuous #GOT\u2026 https://t.co/UMOG4r43hN'), (u'Wed May 23 16:29:41 +0000 2018', u'Is the worst of it over? \U0001f43b\U0001f937\u200d\u2642\ufe0f\n\u2022\n\u2022\n\u2022\n#cryptocurrency #investment #investing #money #crypto #bitcoin #etherium\u2026 https://t.co/pUlv931BTL'), (u'Wed May 23 16:15:47 +0000 2018', u'RT @hashcard: A BLOCKCHAIN-BASED PLATFORM FOR INSURANCE IS BEING CREATED IN HONG-KONG\n\n#hashcard #bitcoin #cryptocurency #trade #trading #i\u2026'), (u'Wed May 23 16:00:35 +0000 2018', u'RT @sniperstube: #GoldmanSachs is already busy setting up a #Bitcoin #trading operation!\n\n#crypto #cryptocurrency #cryptotrading #BTC $BTC\u2026'), (u'Wed May 23 15:59:29 +0000 2018', u'RT @DaveSimonoff: $BTC reached my second target at 8.6k (thanks to #Tether) and retraced back to the previous support line of 7.8-7.9k. Nex\u2026'), (u'Wed May 23 15:36:19 +0000 2018', u'Really nice read from @CryptoShillNye - "These are the people that get rekt in crypto..." - A change from some of t\u2026 https://t.co/6mHGGtM0KT'), (u'Wed May 23 15:18:53 +0000 2018', u"BitCoin Declared #Halal - Wasn't even aware a debate was needed. - Great to see! - https://t.co/gaVz92ky7y\n\n#BTC\u2026 https://t.co/Duq3AJay3Z"), (u'Wed May 23 14:43:35 +0000 2018', u'RT @sniperstube: #GoldmanSachs is already busy setting up a #Bitcoin #trading operation!\n\n#crypto #cryptocurrency #cryptotrading #BTC $BTC\u2026'), (u'Wed May 23 14:40:00 +0000 2018', u'RT @KingCrypto_: FREE Guide: 50 Ways To Make Money With Cryptocurrency\n\nhttps://t.co/n7TnHUmCLv\n\n#cryptocurrency #bitcoin #blockchain #cryp\u2026'), (u'Wed May 23 14:23:49 +0000 2018', u'RT @thecryptomofo: Did somebody say Malta? #Binance #Malta \U0001f44a\U0001f3fd\U0001f911\U0001f680\n\nNO #FEAR, NO #FOMO, NO #FUD  I do #HODL and I ALWAYS $DYOR !!!  \U0001f44a\U0001f3fd\U0001f911\u2764\ufe0f #hod\u2026'), (u'Wed May 23 14:23:38 +0000 2018', u'RT @thecryptomofo: Did somebody say Malta? #Binance #Malta \U0001f44a\U0001f3fd\U0001f911\U0001f680\n\nNO #FEAR, NO #FOMO, NO #FUD  I do #HODL and I ALWAYS $DYOR !!!  \U0001f44a\U0001f3fd\U0001f911\u2764\ufe0f #hod\u2026'), (u'Wed May 23 14:23:27 +0000 2018', u'RT @thecryptomofo: Did somebody say Malta? #Binance #Malta \U0001f44a\U0001f3fd\U0001f911\U0001f680\n\nNO #FEAR, NO #FOMO, NO #FUD  I do #HODL and I ALWAYS $DYOR !!!  \U0001f44a\U0001f3fd\U0001f911\u2764\ufe0f #hod\u2026'), (u'Wed May 23 14:23:09 +0000 2018', u'RT @thecryptomofo: Did somebody say Malta? #Binance #Malta \U0001f44a\U0001f3fd\U0001f911\U0001f680\n\nNO #FEAR, NO #FOMO, NO #FUD  I do #HODL and I ALWAYS $DYOR !!!  \U0001f44a\U0001f3fd\U0001f911\u2764\ufe0f #hod\u2026'), (u'Wed May 23 14:22:59 +0000 2018', u'RT @thecryptomofo: Did somebody say Malta? #Binance #Malta \U0001f44a\U0001f3fd\U0001f911\U0001f680\n\nNO #FEAR, NO #FOMO, NO #FUD  I do #HODL and I ALWAYS $DYOR !!!  \U0001f44a\U0001f3fd\U0001f911\u2764\ufe0f #hod\u2026'), (u'Wed May 23 14:22:48 +0000 2018', u'RT @thecryptomofo: Did somebody say Malta? #Binance #Malta \U0001f44a\U0001f3fd\U0001f911\U0001f680\n\nNO #FEAR, NO #FOMO, NO #FUD  I do #HODL and I ALWAYS $DYOR !!!  \U0001f44a\U0001f3fd\U0001f911\u2764\ufe0f #hod\u2026'), (u'Wed May 23 14:22:28 +0000 2018', u'RT @thecryptomofo: Did somebody say Malta? #Binance #Malta \U0001f44a\U0001f3fd\U0001f911\U0001f680\n\nNO #FEAR, NO #FOMO, NO #FUD  I do #HODL and I ALWAYS $DYOR !!!  \U0001f44a\U0001f3fd\U0001f911\u2764\ufe0f #hod\u2026'), (u'Wed May 23 14:22:00 +0000 2018', u'Did somebody say Malta? #Binance #Malta \U0001f44a\U0001f3fd\U0001f911\U0001f680\n\nNO #FEAR, NO #FOMO, NO #FUD  I do #HODL and I ALWAYS $DYOR !!!  \U0001f44a\U0001f3fd\U0001f911\u2764\ufe0f\u2026 https://t.co/tX2Rv0G4Aw'), (u'Wed May 23 13:54:21 +0000 2018', u'RT @bamitav: "Why are there so many #Russians involved in crypto and #ICOs? \u2014 Quartz" https://t.co/hDlaADucjr #Bitcoin #Blockchain #CryptoC\u2026'), (u'Wed May 23 13:27:28 +0000 2018', u'RT @sniperstube: #GoldmanSachs is already busy setting up a #Bitcoin #trading operation!\n\n#crypto #cryptocurrency #cryptotrading #BTC $BTC\u2026'), (u'Wed May 23 12:17:18 +0000 2018', u'RT @ccjunky77: click here: https://t.co/EKpk3Wbekt\n\n#crypto #trading #altcoin #altcoins #bitcoin #cryptocurrency #btc #blockchain #CryptoNe\u2026'), (u'Wed May 23 12:13:39 +0000 2018', u'I only regret to not have more money to invest \n\n#cryptocurrency #Crypto #cryptotrading #cryptocurrencies #bitcoin\u2026 https://t.co/5uWYr6ve3t'), (u'Wed May 23 11:31:00 +0000 2018', u'RT @KingCrypto_: 7 Cryptocurrency Books You Need To Read! https://t.co/FtDywwdu08\n\n#cryptocurrency #bitcoin #blockchain #crypto #btc #tradi\u2026'), (u'Wed May 23 10:50:29 +0000 2018', u'RT @RealCryptoLion: Throwback: this was posted on Reddit 5 years ago, when 1 Bitcoin was only $10. \n\n#crypto #altcoins #btc #bitcoin $btc #\u2026'), (u'Wed May 23 10:22:38 +0000 2018', u'#Crypto Market Sees Red as Bears Take Control https://t.co/l0alhNKx3K \u2026 #bitcoin #redday #cryptocurrency\u2026 https://t.co/gfLHMYXwlz'), (u'Wed May 23 09:02:10 +0000 2018', u'Lack Of Knowledge About Cryptocurrency No Barrier For Building Digital Assets https://t.co/PU06eVUK4n via\u2026 https://t.co/2QNdU8Yllz'), (u'Wed May 23 08:46:42 +0000 2018', u'RT @CapitalTA: #zil $zil #zilliqa \nGaining strength\n\nTook trendline support\nMA bullish crossover\nMACD bullish crossover \nFalling wedge brea\u2026'), (u'Wed May 23 08:36:56 +0000 2018', u'Bitcoin\u2019s been Forked 44 Times Since Bitcoin Cash: We Explore the Ten Strangest Forks\n#Bitcoin #cryptocurrency\u2026 https://t.co/Msm2exZ6Y7'), (u'Wed May 23 08:36:00 +0000 2018', u'RT @KingCrypto_: 10 Easy Ways To Decide Which Cryptocurrency To Invest In! https://t.co/Qt5Jnvi83F\n\n#cryptocurrency #bitcoin #blockchain #c\u2026'), (u'Wed May 23 08:24:05 +0000 2018', u'RT @DaveSimonoff: $BTC reached my second target at 8.6k (thanks to #Tether) and retraced back to the previous support line of 7.8-7.9k. Nex\u2026'), (u'Wed May 23 08:23:29 +0000 2018', u'RT @DaveSimonoff: $BTC reached my second target at 8.6k (thanks to #Tether) and retraced back to the previous support line of 7.8-7.9k. Nex\u2026'), (u'Wed May 23 08:22:39 +0000 2018', u'RT @DaveSimonoff: $BTC reached my second target at 8.6k (thanks to #Tether) and retraced back to the previous support line of 7.8-7.9k. Nex\u2026'), (u'Wed May 23 08:19:37 +0000 2018', u'RT @DaveSimonoff: $BTC reached my second target at 8.6k (thanks to #Tether) and retraced back to the previous support line of 7.8-7.9k. Nex\u2026'), (u'Wed May 23 08:14:30 +0000 2018', u'New Crypto Pump Channel #Crypto #cryptotrading #ICOs #BTC #binance #EXCHANGE #bounty #bitcoin #Cryptopia #yobit\u2026 https://t.co/bNrzEK77mC'), (u'Wed May 23 08:13:27 +0000 2018', u'#bitcoin #cryptotrading #crypto #cryptocurrencies #BTC IDEA... made simple. https://t.co/kReTimCu0r'), (u'Wed May 23 08:10:38 +0000 2018', u'$BTC reached my second target at 8.6k (thanks to #Tether) and retraced back to the previous support line of 7.8-7.9\u2026 https://t.co/6DeHhGtWPb'), (u'Wed May 23 07:59:22 +0000 2018', u'#crypto #trading #altcoin #altcoins #bitcoin #cryptocurrency #btc #blockchain #CryptoNews #eth #tradingcrypto #ltc\u2026 https://t.co/aVq4PzCl5U'), (u'Wed May 23 07:32:02 +0000 2018', u'click here: https://t.co/EKpk3Wbekt\n\n#crypto #trading #altcoin #altcoins #bitcoin #cryptocurrency #btc #blockchain\u2026 https://t.co/2P1Pu5EUXW'), (u'Wed May 23 06:32:04 +0000 2018', u'Click here" https://t.co/v36350BeYA\n\n#crypto #trading #altcoin #altcoins #bitcoin #cryptocurrency #btc #blockchain\u2026 https://t.co/5ltuUTP4Cw'), (u'Wed May 23 05:24:58 +0000 2018', u'Nobel Prize Economist Says That Crypto the Latest in a Pattern of Alternative Currencies\n#Cryptocurrency\u2026 https://t.co/cEoBk7jski'), (u'Wed May 23 05:00:01 +0000 2018', u'RT @KingCrypto_: 8 Crucial Reasons Why Privacy Coins Will Be HUGE\n\nhttps://t.co/zhihSnZo5s\n\n#cryptocurrency #bitcoin #blockchain #crypto #b\u2026'), (u'Wed May 23 04:31:01 +0000 2018', u'Click here: https://t.co/zPIv2Af83n\n\n#crypto #trading #altcoin #altcoins #bitcoin #cryptocurrency #btc #blockchain\u2026 https://t.co/QFlHUigZ32'), (u'Wed May 23 04:26:29 +0000 2018', u'RT @bamitav: "Why are there so many #Russians involved in crypto and #ICOs? \u2014 Quartz" https://t.co/hDlaADucjr #Bitcoin #Blockchain #CryptoC\u2026'), (u'Wed May 23 03:50:23 +0000 2018', u'RT @ccjunky77: Click here:  https://t.co/xgyY9kwr0v\n\n#crypto #trading #altcoin #altcoins #bitcoin #cryptocurrency #btc #blockchain #CryptoN\u2026'), (u'Wed May 23 03:28:51 +0000 2018', u'RT @ccjunky77: Click here: https://t.co/mqn2lcpzDL\n\n#crypto #trading #altcoin #altcoins #bitcoin #cryptocurrency #btc #blockchain #CryptoNe\u2026'), (u'Wed May 23 03:03:22 +0000 2018', u'RT @Apex_Capital: $SING: #strongbuy, #billiondollarmarket, #buy, #potstocks, #blockchain, #medicalmarijuana, #cannabis, #healthcare, #weedc\u2026'), (u'Wed May 23 02:41:58 +0000 2018', u'$SING: #strongbuy, #billiondollarmarket, #buy, #potstocks, #blockchain, #medicalmarijuana, #cannabis, #healthcare,\u2026 https://t.co/0zE9mCSgzj'), (u'Wed May 23 02:36:03 +0000 2018', u'Click here: https://t.co/mqn2lcpzDL\n\n#crypto #trading #altcoin #altcoins #bitcoin #cryptocurrency #btc #blockchain\u2026 https://t.co/GnKyUaifDm'), (u'Wed May 23 02:27:52 +0000 2018', u'RT @hashcard: Mastercard to Hire More #Blockchain #Specialists\n\n#hashcard #bitcoin #cryptocurency #trade #trading #investing\n#invest #btc #\u2026'), (u'Wed May 23 02:00:02 +0000 2018', u'RT @KingCrypto_: Thinking Of Investing In OmiseGo? Watch This First\n\nhttps://t.co/FboVS6kbhv\n\n#cryptocurrency #bitcoin #blockchain #crypto\u2026'), (u'Wed May 23 01:36:02 +0000 2018', u'Click here:  https://t.co/xgyY9kwr0v\n\n#crypto #trading #altcoin #altcoins #bitcoin #cryptocurrency #btc #blockchain\u2026 https://t.co/i0wWazyeOU'), (u'Tue May 22 23:52:01 +0000 2018', u'RT @RealCryptoLion: If you are new to crypto. Here a nice overview of all the terms: \n\n#crypto #altcoins #btc #bitcoin $btc #CryptoNews #xv\u2026'), (u'Tue May 22 23:48:39 +0000 2018', u'Throwback: this was posted on Reddit 5 years ago, when 1 Bitcoin was only $10. \n\n#crypto #altcoins #btc #bitcoin\u2026 https://t.co/BPw9HdYSx2'), (u'Tue May 22 23:35:03 +0000 2018', u'Click here: https://t.co/a9pBv0C0eE\n\n#crypto #trading #altcoin #altcoins #bitcoin #cryptocurrency #btc #blockchain\u2026 https://t.co/0D0eGBJ6Ti'), (u'Tue May 22 23:00:02 +0000 2018', u'RT @KingCrypto_: Should You Invest In OmiseGo In 2018? Read This Before Investing... https://t.co/9EMboUMjAt\n\n#cryptocurrency #bitcoin #blo\u2026'), (u'Tue May 22 22:35:04 +0000 2018', u'Click here: https://t.co/sMJryVaRK3\n\n#crypto #trading #altcoin #altcoins #bitcoin #cryptocurrency #btc #blockchain\u2026 https://t.co/eOvVnQBopG'), (u'Tue May 22 22:19:00 +0000 2018', u'RT @NOTIFINANCE: Our hot coins for tuesday! Check out https://t.co/vdmlfGiroA #notifinance #crypto #cryptotrading #cryptocurrency #daytradi\u2026'), (u'Tue May 22 21:57:00 +0000 2018', u'RT @WPIBC: Fantastic Idea by @coindesk - A real time price tracker, on just how much Laszlo Hanyecz pizza purchase is now worth! - #Bitcoin\u2026'), (u'Tue May 22 21:34:05 +0000 2018', u'Click here: https://t.co/kyceDYDIiD\n\n#crypto #trading #altcoin #altcoins #bitcoin #cryptocurrency #btc #blockchain\u2026 https://t.co/tFpnm37pT0'), (u'Tue May 22 20:46:12 +0000 2018', u'RT @RealCryptoLion: 1 year crypto trading is 10 year in stock market. \n\n#crypto #altcoins #btc #bitcoin $btc #CryptoNews #xvgfam #vergefam\u2026'), (u'Tue May 22 20:21:11 +0000 2018', u'MyBit Token price has increased 51,5% within last hour. @MyBit_DApp #mybittoken #mybit #cryptotrading #crypto\u2026 https://t.co/YASm1TMrl1'), (u'Tue May 22 20:00:11 +0000 2018', u'RT @WPIBC: Fantastic Idea by @coindesk - A real time price tracker, on just how much Laszlo Hanyecz pizza purchase is now worth! - #Bitcoin\u2026'), (u'Tue May 22 18:43:19 +0000 2018', u'RT @bamitav: "Why are there so many #Russians involved in crypto and #ICOs? \u2014 Quartz" https://t.co/hDlaADucjr #Bitcoin #Blockchain #CryptoC\u2026'), (u'Tue May 22 18:30:01 +0000 2018', u'RT @KingCrypto_: Is Crypto Right For You? Find Out Below:\n\nhttps://t.co/JShdCWGcGP\n\n#cryptocurrency #bitcoin #blockchain #crypto #btc #trad\u2026'), (u'Tue May 22 18:29:31 +0000 2018', u'Getting sucked into it in the first place! :) - #BTC #ETH #XRP #TRX #XYO \n\n#Bitcoin #Crypto #cryptocurrencies\u2026 https://t.co/ebv5mWJqr0'), (u'Tue May 22 17:59:30 +0000 2018', u'An ever increasing problem. @cryptomanran - @jack Get this looked at ASAP! - #Bitcoin #Crypto #cryptocurrencies\u2026 https://t.co/2Y4VHE8mxv'), (u'Tue May 22 17:55:44 +0000 2018', u"RT @WPIBC: Love what @PhilakoneCrypto produces. Clear, concise, and very easy to follow! - Check him out if you haven't already Crypto Fam!\u2026"), (u'Tue May 22 17:08:00 +0000 2018', u'RT @KingCrypto_: Want to get in the crypto game? Sign up to Coinbase &amp; get $10 of free Bitcoin \n\n\U0001f449https://t.co/r5gSTrUkWR\n\n#cryptocurrency\u2026'), (u'Tue May 22 17:02:45 +0000 2018', u"Shout out to @CryptoVanessa - Anyone wanting to get into Crypto, you can't go wrong following some of the ace stuff\u2026 https://t.co/4SkTVbSErU"), (u'Tue May 22 16:59:21 +0000 2018', u"Love what @PhilakoneCrypto produces. Clear, concise, and very easy to follow! - Check him out if you haven't alread\u2026 https://t.co/do87ZLf6WI"), (u'Tue May 22 16:53:38 +0000 2018', u'Fantastic Idea by @coindesk - A real time price tracker, on just how much Laszlo Hanyecz pizza purchase is now wort\u2026 https://t.co/6t4vnNBrAL'), (u'Tue May 22 16:46:09 +0000 2018', u"Happy #WorldGothDay - To all Bitcoin loving Goth's out there! - Make it a double celebration with #BitcoinPizzaDay\u2026 https://t.co/4d3hhbLBqB"), (u'Tue May 22 16:12:28 +0000 2018', u"RT @bethereumteam: Got your #ETH ready? In our public #presale, we aren't limiting anyone! \U0001f680\nRegister to get notified by email: https://t.c\u2026"), (u'Tue May 22 15:18:09 +0000 2018', u'RT @hashcard: AirAsia Announces Plan To Bring Loyalty Program To The #Blockchain\n\n#hashcard #bitcoin #cryptocurency #trade #trading #invest\u2026'), (u'Tue May 22 14:40:59 +0000 2018', u'"Why are there so many #Russians involved in crypto and #ICOs? \u2014 Quartz" https://t.co/hDlaADucjr #Bitcoin\u2026 https://t.co/sWHWY6g4SM'), (u'Tue May 22 14:29:21 +0000 2018', u'RT @ProducToken: The MORE you INVEST, the HIGHER is your BONUS ! \nUP to 35% \U0001f4b0\U0001f4b0\U0001f4b0\nINVEST NOW -&gt; https://t.co/4So9Aym8Gn    \n\n#crypto #tokensa\u2026'), (u'Tue May 22 14:04:38 +0000 2018', u'Sounds like @fundstrat has the right idea @crypto - To the Moon! \n\n#ToTheMOON \n\n#Bitcoin #Crypto #cryptocurrencies\u2026 https://t.co/znFoYMpSPO'), (u'Tue May 22 13:47:50 +0000 2018', u'Happy Bitcoin Pizza Day Everyone!\n\n \U0001f355 \U0001f355 \U0001f355 \U0001f355 \U0001f355\n\n10000 #BTC for a pizza!\n\n#Bitcoin #Crypto #cryptocurrencies\u2026 https://t.co/D4vIhk9Q5O'), (u'Tue May 22 13:31:01 +0000 2018', u'RT @sniperstube: It hurts everytime \U0001f62d\n\n#ethereum #bitcoin #cryptocurrency #cryptotrade #blockchain #cryptolife #altcoins #income #cryptomin\u2026'), (u'Tue May 22 13:30:31 +0000 2018', u'RT @sniperstube: It hurts everytime \U0001f62d\n\n#ethereum #bitcoin #cryptocurrency #cryptotrade #blockchain #cryptolife #altcoins #income #cryptomin\u2026'), (u'Tue May 22 13:09:39 +0000 2018', u'RT @KingCrypto_: Want to learn how to trade crypto? Check out my FREE mini course here:\n\nhttps://t.co/Q37QcXrvmN\n\n#cryptocurrency #bitcoin\u2026'), (u'Tue May 22 12:51:13 +0000 2018', u'RT @NOTIFINANCE: Our hot coins for tuesday! Check out https://t.co/vdmlfGiroA #notifinance #crypto #cryptotrading #cryptocurrency #daytradi\u2026'), (u'Tue May 22 12:48:48 +0000 2018', u'Our hot coins for tuesday! Check out https://t.co/vdmlfGiroA #notifinance #crypto #cryptotrading #cryptocurrency\u2026 https://t.co/TtSk3E9yRC'), (u'Tue May 22 11:49:50 +0000 2018', u'RT @sniperstube: It hurts everytime \U0001f62d\n\n#ethereum #bitcoin #cryptocurrency #cryptotrade #blockchain #cryptolife #altcoins #income #cryptomin\u2026'), (u'Tue May 22 11:49:19 +0000 2018', u'RT @sniperstube: It hurts everytime \U0001f62d\n\n#ethereum #bitcoin #cryptocurrency #cryptotrade #blockchain #cryptolife #altcoins #income #cryptomin\u2026')]



for item in obtain_tweet_sentiment(tweets):
	print item
	print "\n"