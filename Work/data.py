import re
import emoji

def remove_hashtags(data):
    tags = re.compile('(\s*)#bragging(\s*)')
    return re.sub(tags, '', data)

def demojize(data):
    data = emoji.demojize(data)
    return data

def remove_emojis(data):
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, 'demojize', data)

def getData():
    return [
        {
        "edit_history_tweet_ids": [
            "1602154561505992753"
        ],
        "id": "1602154561505992753",
        "text": "TIFU by getting drunk after being sober for 8 months\nA little back story. I started drinking from a very early stage of my life (definitely not proud of it). I didn’t think I had a drinking problem since I’d only drink on “special occasions”, but whenever that happened it wa…"
        },
        {
        "edit_history_tweet_ids": [
            "1602154559635591168"
        ],
        "id": "1602154559635591168",
        "text": "RT @isthisamrita: Happy 14 years in the industry @kkundrra.\nFrom Arjun Punj to your most recent endeavour, it has been a journey of differe…"
        },
        {
        "edit_history_tweet_ids": [
            "1602154557676847105"
        ],
        "id": "1602154557676847105",
        "text": "RT @AdelaEsqueda9: Normally it takes 2 years to get an associates, it took my dad about 5 years, he struggled so much reading and writing e…"
        },
        {
        "edit_history_tweet_ids": [
            "1602154557299388418"
        ],
        "id": "1602154557299388418",
        "text": "HOW CUTEE FFF?????!!! INII LUCUU BANGETTTTT!!!! i'm proud of you too javv🫶🫶 https://t.co/d7LE1P6nrX"
        },
        {
        "edit_history_tweet_ids": [
            "1602154555889926144"
        ],
        "id": "1602154555889926144",
        "text": "RT @AdelaEsqueda9: Normally it takes 2 years to get an associates, it took my dad about 5 years, he struggled so much reading and writing e…"
        },
        {
        "edit_history_tweet_ids": [
            "1602154554421874690"
        ],
        "id": "1602154554421874690",
        "text": "@hendaeriv Nope not proud at all. I also said this but seems nobody read it so here . Aku tau kekuranganku kok dan im working on it https://t.co/L1CSAXh12B"
        },
        {
        "edit_history_tweet_ids": [
            "1602154551544811520"
        ],
        "id": "1602154551544811520",
        "text": "RT @sneakyseunie: @JacksonWang852 YES SIR I ABSOLUTELY LOVE IT 🎠🎪\nwhatever happens, \nknow that your Jackys sees all your hard works and eff…"
        },
        {
        "edit_history_tweet_ids": [
            "1602154550823161857"
        ],
        "id": "1602154550823161857",
        "text": "RT @DatttBitchhh_: So proud of me &amp; how i’ve been handling shit lately ."
        },
        {
        "edit_history_tweet_ids": [
            "1602154542610751490"
        ],
        "id": "1602154542610751490",
        "text": "@awwsome_juan @MarioALNG @MLS_Buzz It’s literally not. 🤦‍♂️ I’m done dude. I’m proud of you learning English but you’ve gotta do better. You’re not there yet"
        },
        {
        "edit_history_tweet_ids": [
            "1602154538852458497"
        ],
        "id": "1602154538852458497",
        "text": "Gutless #LyinLuxon crying \"I wasn't, I didn't, I'm not\" AGAIN when caught out behind racist, pretending because he worked @ AirNZ @ the airport he knows all about &amp; LOVES South Auckland. But proud, decent South Aucklander Sio is having none of his dog whistle racism. https://t.co/iXLWzjOXtl https://t.co/YoQVTfRInS"
        },
        {
        "edit_history_tweet_ids": [
            "1602154710714421250"
        ],
        "id": "1602154710714421250",
        "text": "@jodecicry I thought it was cunnilingus so I’m really glad to find out it’s not"
        },
        {
        "edit_history_tweet_ids": [
            "1602154698500628480"
        ],
        "id": "1602154698500628480",
        "text": "@elonmusk @StationCDRKelly I'm just glad you're not left or right-wing, but rather some third thing (right-wing). Good job apartheid boy."
        },
        {
        "edit_history_tweet_ids": [
            "1602154696646565890"
        ],
        "id": "1602154696646565890",
        "text": "\"  so you heard that  ?  i'm \nso glad you have ears  , \nmy cariño  .  \"  poking the \nother's shoulder back  ── \nin a playful mood .  \"  you\nentertain so well .  \" https://t.co/KwWCGNTZvO"
        },
        {
        "edit_history_tweet_ids": [
            "1602154694931255296"
        ],
        "id": "1602154694931255296",
        "text": "@WeeabooJudas I really do love this about arknights, I'm glad there's SO much content waiting for me whenever I have the time to dive in. What a good game."
        },
        {
        "edit_history_tweet_ids": [
            "1602154692594864129"
        ],
        "id": "1602154692594864129",
        "text": "Cod I'm glad none of my partners were around to witness that—."
        },
        {
        "edit_history_tweet_ids": [
            "1602154690849947648"
        ],
        "id": "1602154690849947648",
        "text": "I’ll be glad when  Christmas is over 😩"
        },
        {
        "edit_history_tweet_ids": [
            "1602154689340096512"
        ],
        "id": "1602154689340096512",
        "text": "@MamaGrian We love you too, Stauber!! I’m glad we’ve been able to help you as much as you’ve helped us without knowing. Mwa Mwa Mwa"
        },
        {
        "edit_history_tweet_ids": [
            "1602154689058963456"
        ],
        "id": "1602154689058963456",
        "text": "Agree, it was masterful and I love all the acclaim she's getting on here tonight. I don't though think it was in character for Ethan to follow her so I am glad that was left vague. https://t.co/i9ulzY91MA"
        },
        {
        "edit_history_tweet_ids": [
            "1602154688782032896"
        ],
        "id": "1602154688782032896",
        "text": "@raiwist @sportbible Glad I didn’t have to be the one to say it lol"
        },
        {
        "edit_history_tweet_ids": [
            "1602154687012245504"
        ],
        "id": "1602154687012245504",
        "text": "Glad I brought my Polteageist w/Protect cause gdamn that pokemon was just BULLYING me with Dark Pulse. I HATE that the raid pokemon single you out &amp; just spam their super effective moves on you."
        },
        {
        "edit_history_tweet_ids": [
            "1602154946752831489"
        ],
        "id": "1602154946752831489",
        "text": "@michaelmalice Wow, I'm surprised that happened. He probably should've asked for better odds. I'm happy for Tom Woods that he is broadly trusted by the internet."
        },
        {
        "edit_history_tweet_ids": [
            "1602154946434109442"
        ],
        "id": "1602154946434109442",
        "text": "@mochirin_arin sweetest arin, happy birthday to you (ﾉ´ヮ´)ﾉ*:･ﾟ✧ i’m not good at writing birthday messages but i hope you have a wonderful day! love you! https://t.co/7FrhaifaLY"
        },
        {
        "edit_history_tweet_ids": [
            "1602154944693694464"
        ],
        "id": "1602154944693694464",
        "text": "RT @Aoythanaporn1: Have a good holiday and have fun with your family 😍💜💖🐍 \nMorning12🌈🎐 BamBam💜\n\nI Love Songs  #SlowMo, #WhoAreYou \nand #Whe…"
        },
        {
        "edit_history_tweet_ids": [
            "1602154943590592512"
        ],
        "id": "1602154943590592512",
        "text": "RT @sukrot_wilaiwan: Morning12  BamBam 🍋\nI like Song  #SlowMo #WhoAreYou and #WheelsUp #riBBon by #BamBam @BamBam1A . Happy to listening. @…"
        },
        {
        "edit_history_tweet_ids": [
            "1602154942923476992"
        ],
        "id": "1602154942923476992",
        "text": "All I want for Christmas is to be happy yo .."
        },
        {
        "edit_history_tweet_ids": [
            "1602154941543776256"
        ],
        "id": "1602154941543776256",
        "text": "“ .. I .. I- I want him to be ok too ... It feels too cruel to just leave him .. I know he wants me to be happy - but .. does he not realize that it hurts me to see him like this ? “ https://t.co/Hs7bNP6ylZ"
        },
        {
        "edit_history_tweet_ids": [
            "1602154941321285632"
        ],
        "id": "1602154941321285632",
        "text": "RT @GenesisXlivia: i still love drawing xen for yall and im happy i got a bunch of you to like the official design, but when shei starts ma…"
        },
        {
        "edit_history_tweet_ids": [
            "1602154940474036224"
        ],
        "id": "1602154940474036224",
        "text": "RT @jespinoza0025: Happy Sunday! It was a tough week I got  sick again but I promise I’ll spam y’all with public content soon😭. #studytwtph…"
        },
        {
        "edit_history_tweet_ids": [
            "1602154939853475840"
        ],
        "id": "1602154939853475840",
        "text": "RT @amourlisaa: I hate when y’all post everyone dm of them telling y’all happy birthday"
        },
        {
        "edit_history_tweet_ids": [
            "1602154939245264896"
        ],
        "id": "1602154939245264896",
        "text": "I streaming #SlowMo, #WhoAreYou and #WheelsUp by #BamBam on Spotify @BamBam1A make me feel so happy the music is so catchy and beautiful 💕"
        },
        {
        "edit_history_tweet_ids": [
            "1602154938767142913"
        ],
        "id": "1602154938767142913",
        "text": "RT @sentacoumar: I don’t know how to honor you on this day other than by letting you know how much I miss you and wish you were still here.…"
        },
        {
        "edit_history_tweet_ids": [
            "1602154936867094528"
        ],
        "id": "1602154936867094528",
        "text": "RT @SidNaaz_Forever: Thinking about the bond between Sidharth &amp; Rita aunty makes me both emotional &amp; happy like I can’t really explain what…"
        },
        {
        "edit_history_tweet_ids": [
            "1602154935139078147"
        ],
        "id": "1602154935139078147",
        "text": "Team BamBam 97\nI like Song  #SlowMo #WhoAreYou and #WheelsUp #riBBon by #BamBam @BamBam1A . Happy to listening. @BAMBAMxABYSS\nAnd waiting for BB3.  19"
        },
        {
        "edit_history_tweet_ids": [
            "1602154932462837760"
        ],
        "id": "1602154932462837760",
        "text": "RT @CannabisLover95: Watching @dope_as_yola_ and what I love about your videos is that’s it’s like kicking it with the homie… I love that y…"
        },
        {
        "edit_history_tweet_ids": [
            "1602154931322249216"
        ],
        "id": "1602154931322249216",
        "text": "RT @justcrxa: [ @mscrizataa IG story ]\n\n“happy happy birthday ate ko!🤎 \nyour beautiful soul deserves every beautiful thing in this world. I…"
        },
        {
        "edit_history_tweet_ids": [
            "1602154931091300353"
        ],
        "id": "1602154931091300353",
        "text": "RT @MissConstrued13: Good boys make Me happy\nI love waking up and seeing who has tipped My LF looping clip stream.\n\nI want to see more of y…"
        },
        {
        "edit_history_tweet_ids": [
            "1602154930579570688"
        ],
        "id": "1602154930579570688",
        "text": "RT @WantSomeOnika_: Happy birthday to my baby @statsofminaj i love you so much! So thankful to have met you, your a blast every time we lin…"
        },
        {
        "edit_history_tweet_ids": [
            "1602154930403704832"
        ],
        "id": "1602154930403704832",
        "text": "Team BamBam 97\nI like Song  #SlowMo #WhoAreYou and #WheelsUp #riBBon by #BamBam @BamBam1A . Happy to listening. @BAMBAMxABYSS\nAnd waiting for BB3.  18"
        },
        {
        "edit_history_tweet_ids": [
            "1602154929098891264"
        ],
        "id": "1602154929098891264",
        "text": "RT @hourlysid: #HBDSidharthShukla: This is How, I will Remember him, All Happy-goofy Smiling, Forever and Always!💫🌟♥️\nhttps://t.co/EkPWVQOm…"
        },
        {
        "edit_history_tweet_ids": [
            "1602154925580062723"
        ],
        "id": "1602154925580062723",
        "text": "RT @sponge_enjoyer: 420 followers??? I've peaked as a human now, I can die happy. Here's some SquidBobbery! https://t.co/nzQikpRZeI"
        },
        {
        "edit_history_tweet_ids": [
            "1602155070069563392"
        ],
        "id": "1602155070069563392",
        "text": "RT @almostdita: Knowing that they released an official statement that he will not be greeting fans and media, the picture that he shared wi…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155069771767808"
        ],
        "id": "1602155069771767808",
        "text": "@Everdome_io One of the best companies I've ever met, the company owner and the employee are very good! #Everdome #TheJourneyHasBegun\n\n@h_bashar007 @Foakay_ @SynapseMerch"
        },
        {
        "edit_history_tweet_ids": [
            "1602155069537153029"
        ],
        "id": "1602155069537153029",
        "text": "I believe this is a faithful project. The project has a lot of attractions so hopefully the project will be better in the future and will be the best.\n@anton_wijack @hanz_153 @edoyuanda123\n#Apelion #NFTs #NFTGiveaways https://t.co/31P85l3i4u"
        },
        {
        "edit_history_tweet_ids": [
            "1602155069406728192"
        ],
        "id": "1602155069406728192",
        "text": "💙 CIRCE | BANNER 💙\n\nI absolutely love Circe. Gotta be one of the best people I’ve connected with in this space and glad to see her still rocking the banner! Can’t wait to see your major success in this space Circe!! 💚 (@decircusmaster)\n\nPortfolio: https://t.co/b7VGnEpfca https://t.co/XkjuwZqJoD"
        },
        {
        "edit_history_tweet_ids": [
            "1602155068949659648"
        ],
        "id": "1602155068949659648",
        "text": "One of the best takes I've seen all day👇 https://t.co/0QupoEqzY9"
        },
        {
        "edit_history_tweet_ids": [
            "1602155068043804674"
        ],
        "id": "1602155068043804674",
        "text": "RT @scarfedbrit: Disney just submitted this for Best Visual Effects at the Oscars. \n\nI repeat: Best. Visual. Effects. https://t.co/o1dEd0Cp…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155067569999872"
        ],
        "id": "1602155067569999872",
        "text": "RT @ampijimin: r u so jobless 2 hav time 2 attempt 2 drag the best performer over a fun video when both artists r collaborating which has n…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155065808408576"
        ],
        "id": "1602155065808408576",
        "text": "RT @Ashcryptoreal: I try my best to keep giving back to the community in any possible way 🙏"
        },
        {
        "edit_history_tweet_ids": [
            "1602155064570875905"
        ],
        "id": "1602155064570875905",
        "text": "@pkeetsbird @EthicalSkeptic I am a nurse (not data minded) who worked in a covid ICU. I've since given birth to a healthy baby (I refused any boosters and my best friend is also pregnant currently) so there is hope for anyone else in my position 🙂"
        },
        {
        "edit_history_tweet_ids": [
            "1602155062763061248"
        ],
        "id": "1602155062763061248",
        "text": "RT @Indian_BoxOffic: Who is Best Actor??\nLet's settle it 💥💥💥\nhttps://t.co/527gj9Ntaf\n\n#AlluArjun | #JrNTR | #RamCharan https://t.co/nJ8dWQG…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155061563777025"
        ],
        "id": "1602155061563777025",
        "text": "RT @scarfedbrit: Disney just submitted this for Best Visual Effects at the Oscars. \n\nI repeat: Best. Visual. Effects. https://t.co/o1dEd0Cp…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155059936116736"
        ],
        "id": "1602155059936116736",
        "text": "Me every time I link with my friends 🤞❤️ best feeling https://t.co/kq8kp9Excl"
        },
        {
        "edit_history_tweet_ids": [
            "1602155057788731395"
        ],
        "id": "1602155057788731395",
        "text": "RT @Atuhairecarol10: Happy birthday my love @Rachealkyy I wish you nothing but the best on this special day. May this birthday bring you an…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155057511702528"
        ],
        "id": "1602155057511702528",
        "text": "RT @gcfullsun: after finishing season 2 of young royals i can still confidently say this is the best scene ever no one will do it like her…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155057494994944"
        ],
        "id": "1602155057494994944",
        "text": "RT @DeplorableNew: I'm betting it won't happen.  This spoiled/privileged brat learned NOTHING from her recent experience.  Dementia Joe cal…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155057449177090"
        ],
        "id": "1602155057449177090",
        "text": "RT @scarfedbrit: Disney just submitted this for Best Visual Effects at the Oscars. \n\nI repeat: Best. Visual. Effects. https://t.co/o1dEd0Cp…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155057138782208"
        ],
        "id": "1602155057138782208",
        "text": "RT @SidharthkaFan: And at the end of the day I know I did the best I could do....p...\n#HBDSidharthShukla"
        },
        {
        "edit_history_tweet_ids": [
            "1602155055989362688"
        ],
        "id": "1602155055989362688",
        "text": "RT @MissyElliott: Two time Doctorate “Dr. Elliott” I am so Grateful🙏🏾Thank you @Norfolkstate for having me today🙌🏾 To the Class Of 2022” Ma…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155055637233664"
        ],
        "id": "1602155055637233664",
        "text": "RT @dimpleamonds: I’m trying my best. Here are the 4 best screencaps from my video. No watermark, just enjoy. 🥹🫶 https://t.co/2lWkl1ORBA"
        },
        {
        "edit_history_tweet_ids": [
            "1602155055037177857"
        ],
        "id": "1602155055037177857",
        "text": "RT @Leticia35170144: I can’t find words to tell you how grateful l am for your expressions of affection and being present 💝 with your beaut…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155149182570496"
        ],
        "id": "1602155149182570496",
        "text": "RT @thecomicroom: Random Key Issue\nFantastic Four #52 featuring the First Appearance of Black Panther. Another one I got a long time ago. A…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155144417779712"
        ],
        "id": "1602155144417779712",
        "text": "Does it need to be? The gameplay isn't amazing sure,but it has a very strong narrative and set of characters and world that carries it hard. \nI don't see why we shouldn't respect a game that has such a good narrative just because of the whole sony \"\"\"Game\"\"\" thing. https://t.co/Oxif7yMgEQ"
        },
        {
        "edit_history_tweet_ids": [
            "1602155144090877952"
        ],
        "id": "1602155144090877952",
        "text": "RT @Theunnamed_S: How on earth that I miss this amazing picture??? 😵😵😵\n\nD7 FUN PARTY WITH MILEAPO &amp; FANS\n\n#FunFanไปกับD7xMileApo\n@milephakp…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155143499218945"
        ],
        "id": "1602155143499218945",
        "text": "RT @EZE3D: Someone steal these amazing designs to sell them on Mugs and T-Shirts, I really don't care, this is AI art that's been generated…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155142157340672"
        ],
        "id": "1602155142157340672",
        "text": "It's here! Check out now! available @ the party Saw a swirly steak I'm from iowa thanks Amazing shot by."
        },
        {
        "edit_history_tweet_ids": [
            "1602155141582536705"
        ],
        "id": "1602155141582536705",
        "text": "@notcapnamerica I adore my girls. They’re feisty, bold, strong, independent, beautiful, successful, educated, funny, smart and amazing black women."
        },
        {
        "edit_history_tweet_ids": [
            "1602155130128068608"
        ],
        "id": "1602155130128068608",
        "text": "RT @goinggodward: It’s amazing how Jesus, upon entering this world, was both ancient and new. I can’t get over it."
        },
        {
        "edit_history_tweet_ids": [
            "1602155129909690368"
        ],
        "id": "1602155129909690368",
        "text": "@starryoutlaw you’re the best i could ever ask for you’re doing such an amazing job i’m lucky to have you"
        },
        {
        "edit_history_tweet_ids": [
            "1602155125870514183"
        ],
        "id": "1602155125870514183",
        "text": "this the most amazing things I've ever witnessed https://t.co/KWBBRqhynf"
        },
        {
        "edit_history_tweet_ids": [
            "1602155124386066432"
        ],
        "id": "1602155124386066432",
        "text": "@sehunsnoona_ I am so happy that Filipino EXOL were amazing (as usual) and welcomed our Chennie with the reception he deserves. He should have only happiness and light no booing or antis."
        },
        {
        "edit_history_tweet_ids": [
            "1602155118245421057"
        ],
        "id": "1602155118245421057",
        "text": "@kuchikirukia_20 I always loved him, but the episode was amazing so yeah"
        },
        {
        "edit_history_tweet_ids": [
            "1602155117029249024"
        ],
        "id": "1602155117029249024",
        "text": "RT @Ecchisama_: Good afternoon everyone, I hope you all have an amazing day!\nArtist: @gentuki0999 \nhttps://t.co/aR4bWLq3rv https://t.co/oLq…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155115389001730"
        ],
        "id": "1602155115389001730",
        "text": "RT @NostalgicPulls: 🔥🔥GIVEAWAY🔥🔥\n\nThank you all so much for getting me here and forming an amazing community. I hit 1500 sometime in the la…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155114974052354"
        ],
        "id": "1602155114974052354",
        "text": "RT @1A6797: เช้าวันหยุดชดเชย สดชื่นสดใสมีความสุขมากๆนะคะน้องแบมและทุกๆคน\nMorning12 BAMBAM\nBamBam #BamBam  @BamBam1A #뱀뱀  music is amazing e…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155112461484034"
        ],
        "id": "1602155112461484034",
        "text": "RT @EZE3D: Someone steal these amazing designs to sell them on Mugs and T-Shirts, I really don't care, this is AI art that's been generated…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155098569850882"
        ],
        "id": "1602155098569850882",
        "text": "RT @gomezgaIore: Okay now that I had time to process the finale was incredible amazing writing amazing acting all around an amazing show 💗…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155095067705344"
        ],
        "id": "1602155095067705344",
        "text": "RT @daph1908: Guess who received an award last night? Yup, me!! GOD is amazing!! I give HIM all the glory. I LOVE the work that we do as me…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155090512875520"
        ],
        "id": "1602155090512875520",
        "text": "@AlgerianFooty every time I go back to Algiers for a holiday I witness incredible talent, the type you see get into Charlton, Arsenal, Chelsea academies etc, they don't have a convolute system with amazing pitches though, most of these guys are playing alongside an abandoned pool for fun"
        },
        {
        "edit_history_tweet_ids": [
            "1602155089996779520"
        ],
        "id": "1602155089996779520",
        "text": "@shelbygraces Right now I'm just watching all of sailor moon, specifically the English dub that Hulu has because it is so out of pocket sometimes that it makes me love the series even more another good show would be Wednesday just cuse it's amazing"
        },
        {
        "edit_history_tweet_ids": [
            "1602155282624557058"
        ],
        "id": "1602155282624557058",
        "text": "RT @iconickdramas: 4 episodes in and I'm really loving #AlchemyOfSouls! The plot development is amazing, and there are a lot of interesting…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155273984040960"
        ],
        "id": "1602155273984040960",
        "text": "@MarinaVT_ Well I guess I’m going to self simp, because the artist is doing an amazing job, still very much a WIP but what I’ve seen so far, is quite amazing \n\nOh, and I’ll also mention @The_Obsxrver because their model is also really really good https://t.co/Tl3RHF0aS3 https://t.co/jPt4tualav"
        },
        {
        "edit_history_tweet_ids": [
            "1602155259748667393"
        ],
        "id": "1602155259748667393",
        "text": "This was amazing. She absolutely fucked back. Now I gotta change my sheets 😭😭🥴\n\nShe thought I was playing with her short ass when I said when she pull up I’m ware her ass out. 😂🥰 https://t.co/8yDYoEohBr"
        },
        {
        "edit_history_tweet_ids": [
            "1602155242556211202"
        ],
        "id": "1602155242556211202",
        "text": "@Hi_Goldenness Bongjae you guys did amazing I’m so proud of you all💛💛pls take good care of yourselves now and get all the rest you need!!"
        },
        {
        "edit_history_tweet_ids": [
            "1602155239355850752"
        ],
        "id": "1602155239355850752",
        "text": "@_Ch0ke_me_ that’s amazing!! omg I’m so proud you’re doing great dude!!"
        },
        {
        "edit_history_tweet_ids": [
            "1602155201854836737"
        ],
        "id": "1602155201854836737",
        "text": "@diablosellout i understand how u feel but kayla u are worth so much &lt;3 u are so important to so many people and u are doing amazing. i'm so proud of u for still being here in general &amp; i know u can continue to push through. it may just feel like existing right now but one day it'll be living."
        },
        {
        "edit_history_tweet_ids": [
            "1602155201401876482"
        ],
        "id": "1602155201401876482",
        "text": "i love this show so much,,, joonie is such a great host, i love his interventions but all the other guests have great sense of humor too + amazing intellect, i'm really invested 😆 #tdouhk https://t.co/ftqMnPJsoG"
        },
        {
        "edit_history_tweet_ids": [
            "1602155142157340672"
        ],
        "id": "1602155142157340672",
        "text": "It's here! Check out now! available @ the party Saw a swirly steak I'm from iowa thanks Amazing shot by."
        },
        {
        "edit_history_tweet_ids": [
            "1602155129909690368"
        ],
        "id": "1602155129909690368",
        "text": "@starryoutlaw you’re the best i could ever ask for you’re doing such an amazing job i’m lucky to have you"
        },
        {
        "edit_history_tweet_ids": [
            "1602155089996779520"
        ],
        "id": "1602155089996779520",
        "text": "@shelbygraces Right now I'm just watching all of sailor moon, specifically the English dub that Hulu has because it is so out of pocket sometimes that it makes me love the series even more another good show would be Wednesday just cuse it's amazing"
        },
        {
        "edit_history_tweet_ids": [
            "1602155058921086976"
        ],
        "id": "1602155058921086976",
        "text": "@DomTheBombYT Some parts of plague Tale look really good but haven't played that yet either. And so far  for what I've done in God of War Ragnarok, that has some pretty amazing looking moments too from where I'm at in the the game"
        },
        {
        "edit_history_tweet_ids": [
            "1602155055607578624"
        ],
        "id": "1602155055607578624",
        "text": "@HTea101 Probably the only girl that even if will dye her hair in Diarrhoea color will still be f..ing gorgeous not even sure I'm joking you are and always be \"ladies and gentlemen... Her.\" how can one choose when every colors just amazing as f..k on you."
        },
        {
        "edit_history_tweet_ids": [
            "1602155051383803906"
        ],
        "id": "1602155051383803906",
        "text": "RT @brandihough81: I’m heartbroken that you worked so hard for 4 years to get your degree, landed an amazing job, and bought your new Range…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155039086231554"
        ],
        "id": "1602155039086231554",
        "text": "Thank you Lord in advance for my amazing husband! I’m ready to do life, ministry and business with him! Ready to serve! 🙌🏾👏🏾"
        },
        {
        "edit_history_tweet_ids": [
            "1602155010972094464"
        ],
        "id": "1602155010972094464",
        "text": "I'm retweeting this again because it was amazing https://t.co/G7mk3aoEHQ"
        },
        {
        "edit_history_tweet_ids": [
            "1602155003099369472"
        ],
        "id": "1602155003099369472",
        "text": "@snowdorii I need to watch season 6 but I’m waiting for it to be on streaming. First five seasons were so good though totally agree that it’s an amazing work"
        },
        {
        "edit_history_tweet_ids": [
            "1602154981989445632"
        ],
        "id": "1602154981989445632",
        "text": "RT @jayhoonfics_au: \"if any of the Enhypen members were to be a different person, if it wasn’t all seven of us, I really don’t think we wou…"
        },
        {
        "edit_history_tweet_ids": [
            "1602154963907629057"
        ],
        "id": "1602154963907629057",
        "text": "also, Martin Sheen?!?!? I'm already obsessed with this game omg this is gonna be amazing"
        },
        {
        "edit_history_tweet_ids": [
            "1602154950984814592"
        ],
        "id": "1602154950984814592",
        "text": "RT @jayhoonfics_au: \"if any of the Enhypen members were to be a different person, if it wasn’t all seven of us, I really don’t think we wou…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155404414574593"
        ],
        "id": "1602155404414574593",
        "text": "RT @dimpleamonds: I’m trying my best. Here are the 4 best screencaps from my video. No watermark, just enjoy. 🥹🫶 https://t.co/2lWkl1ORBA"
        },
        {
        "edit_history_tweet_ids": [
            "1602155397200101376"
        ],
        "id": "1602155397200101376",
        "text": "i’m so serious when i say Matt Thomas was the best Raptor here https://t.co/TFkx8JfXXX"
        },
        {
        "edit_history_tweet_ids": [
            "1602155390720180229"
        ],
        "id": "1602155390720180229",
        "text": "RT @dimpleamonds: I’m trying my best. Here are the 4 best screencaps from my video. No watermark, just enjoy. 🥹🫶 https://t.co/2lWkl1ORBA"
        },
        {
        "edit_history_tweet_ids": [
            "1602155388861927426"
        ],
        "id": "1602155388861927426",
        "text": "best believe I’m still bejeweled when I walk in the room I can still make the whole place shimmerrr"
        },
        {
        "edit_history_tweet_ids": [
            "1602155375939096577"
        ],
        "id": "1602155375939096577",
        "text": "RT @coffeexheaven: Nahi matalb 2 months hue hain new leads ko aakar imlie mein and imlie ko best show ka award mila vo new leads ko pakda d…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155375809433602"
        ],
        "id": "1602155375809433602",
        "text": "RT @dimpleamonds: I’m trying my best. Here are the 4 best screencaps from my video. No watermark, just enjoy. 🥹🫶 https://t.co/2lWkl1ORBA"
        },
        {
        "edit_history_tweet_ids": [
            "1602155372802105344"
        ],
        "id": "1602155372802105344",
        "text": "RT @JadenHeart3: one of my best friends just told me: \n\nthis was the first vid he ever had a w*nk to ^^\ni'm embarrassed =))) https://t.co/r…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155368276234241"
        ],
        "id": "1602155368276234241",
        "text": "my Girlfriend is the best girlfriend I can ever wish for she’s the best all I’m finna say🧏‍♂️❤️."
        },
        {
        "edit_history_tweet_ids": [
            "1602155353596039171"
        ],
        "id": "1602155353596039171",
        "text": "RT @KyeomsBaekery: ⚔️: what’s with that smile?\n💎: no, just because you’re pretty\n⚔️: huh?\n💎: bcs you’re pretty /laughs\n⚔️: bcs i’m pretty?…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155343353499648"
        ],
        "id": "1602155343353499648",
        "text": "RT @Ladymomoka1: วันนี้แจบอมเดินทางไปทัวร์ยูโรปแล้ว\nHave a safe flight, Jaebeom🥰🌴\nI hope you are not too tired from work. I’m wishing you a…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155343215484928"
        ],
        "id": "1602155343215484928",
        "text": "RT @s_t_gibson: I'm ESPECIALLY reminding all memoir writers and lifestyle writers of this fact; don't give your best ideas to Twitter for f…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155342636486656"
        ],
        "id": "1602155342636486656",
        "text": "Can’t believe I’m still going to work 😩 I should be home living my best life"
        },
        {
        "edit_history_tweet_ids": [
            "1602155332637073409"
        ],
        "id": "1602155332637073409",
        "text": "I’m so far away from home,\nBut I’ve learned that’s the best place for growth."
        },
        {
        "edit_history_tweet_ids": [
            "1602155323120562176"
        ],
        "id": "1602155323120562176",
        "text": "Check out what I'm selling: Customerized Best seller laneige midnight holiday minis lip sleeping mask: Get up to $30 off* when you use my code UFSVAF to sign up for Mercari. *Terms apply #mercari \nhttps://t.co/NNF4Rgd3SC"
        },
        {
        "edit_history_tweet_ids": [
            "1602155316137054209"
        ],
        "id": "1602155316137054209",
        "text": "RT @venusianbabyy: i’m so mentally drained.  but i have too much to lose to not give every day my best shot"
        },
        {
        "edit_history_tweet_ids": [
            "1602155309547536388"
        ],
        "id": "1602155309547536388",
        "text": "RT @adriyoung: hi i’m mark from hinge. i know the best place in town for tacos. first round is on me if it’s tequila. the most spontaneous…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155306313601027"
        ],
        "id": "1602155306313601027",
        "text": "RT @ajaynsp: I Kn0w That I'm n0t The Best...But I Als0 Kn0w That I'M n0t Like The REST....ss.\n\n#HBDSidharthShukla"
        },
        {
        "edit_history_tweet_ids": [
            "1602155302488608768"
        ],
        "id": "1602155302488608768",
        "text": "@JanetJackson Yes I'm hoping and praying that we can be together and I am one of your biggest fans Tammy and God bless you and your whole entire family I will always love you from the bottom of my heart Janet you are my best singer in the whole entire world peace out"
        },
        {
        "edit_history_tweet_ids": [
            "1602155301758803968"
        ],
        "id": "1602155301758803968",
        "text": "RT @RebornGypsy: on some cocky shit, i’m what’s best for you.."
        },
        {
        "edit_history_tweet_ids": [
            "1602155300219650048"
        ],
        "id": "1602155300219650048",
        "text": "RT @dimpleamonds: I’m trying my best. Here are the 4 best screencaps from my video. No watermark, just enjoy. 🥹🫶 https://t.co/2lWkl1ORBA"
        },
        {
        "edit_history_tweet_ids": [
            "1602155353352830981"
        ],
        "id": "1602155353352830981",
        "text": "RT @o_keilani: Gen Z is doing excellent and changing the landscape of what it means to be a professional 😭 they said to hell with everythin…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155271614517248"
        ],
        "id": "1602155271614517248",
        "text": "@nationalpost I'm a USA citizen.\nI just had dental care in Thailand.\nPaid less than US$3000 for what would have cost me over US$10,000 in the USA.\n\nExcellent service.\nPerfect results.\n\n@JustinTrudeau \n#LegacyOfFraud\n\n."
        },
        {
        "edit_history_tweet_ids": [
            "1602155247815868416"
        ],
        "id": "1602155247815868416",
        "text": "RT @o_keilani: Gen Z is doing excellent and changing the landscape of what it means to be a professional 😭 they said to hell with everythin…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155237321887747"
        ],
        "id": "1602155237321887747",
        "text": "@tropicaljewt30 no lol it was rly funny i’m proud to be represented by my excellent tweets 🚨🙈"
        },
        {
        "edit_history_tweet_ids": [
            "1602155125287669764"
        ],
        "id": "1602155125287669764",
        "text": "@fatale_lily Those are some excellent pair of fabulous and Fantastic Big Melons Baby. I'm sorry absolutely for those Beards 🧔. Yet, I'm Glad I tend to shave every week. I wouldn't do that to you Gorgeous. I'd be happy loving them. And that 🔥 Body."
        },
        {
        "edit_history_tweet_ids": [
            "1602155059630022661"
        ],
        "id": "1602155059630022661",
        "text": "@tlachtga Decided I'm picking favorites in anyone's cookie array that gets posted this year. The winner on this table? \n\n(mostly for the excellent use of the full color palette here, which is excellent across the board) https://t.co/xou1BByBks"
        },
        {
        "edit_history_tweet_ids": [
            "1602154944550866945"
        ],
        "id": "1602154944550866945",
        "text": "I’m getting real sick of Awesome Excellent tonight! @jasonffl"
        },
        {
        "edit_history_tweet_ids": [
            "1602154878331416576"
        ],
        "id": "1602154878331416576",
        "text": "RT @DavidGaustad: @Taylor_2023_TT @PL_Wilkins @marisakresge @TopDrawerSoccer @TheSoccerWire @GAcademyLeague @Oliviero21 @WIYouthSoccer @ScW…"
        },
        {
        "edit_history_tweet_ids": [
            "1602154819044904961"
        ],
        "id": "1602154819044904961",
        "text": "RT @o_keilani: Gen Z is doing excellent and changing the landscape of what it means to be a professional 😭 they said to hell with everythin…"
        },
        {
        "edit_history_tweet_ids": [
            "1602154756184903680"
        ],
        "id": "1602154756184903680",
        "text": "Look I’m pretty sure @ImKeithDavid would make an excellent Sith #RickandMorty"
        },
        {
        "edit_history_tweet_ids": [
            "1602154662911963137"
        ],
        "id": "1602154662911963137",
        "text": "RT @o_keilani: Gen Z is doing excellent and changing the landscape of what it means to be a professional 😭 they said to hell with everythin…"
        },
        {
        "edit_history_tweet_ids": [
            "1602154654804189185"
        ],
        "id": "1602154654804189185",
        "text": "I don't watch The White Lotus but I'm seeing it trending on my TL. And immediately I recognized by name Meghann Fahy from the one thing I've seen her in. Psycho Hannah on #OLTL. She was so excellent on there."
        },
        {
        "edit_history_tweet_ids": [
            "1602154127919878147"
        ],
        "id": "1602154127919878147",
        "text": "RT @o_keilani: Gen Z is doing excellent and changing the landscape of what it means to be a professional 😭 they said to hell with everythin…"
        },
        {
        "edit_history_tweet_ids": [
            "1602154019270557698"
        ],
        "id": "1602154019270557698",
        "text": "RT @biza5: @skipadeefarm @dirtvision @whiskeymyers @MaconCentreplex Amazing as always! Great video and sound and I feel almost like I'm the…"
        },
        {
        "edit_history_tweet_ids": [
            "1602153847849455617"
        ],
        "id": "1602153847849455617",
        "text": "I'm your excellent tutor"
        },
        {
        "edit_history_tweet_ids": [
            "1602153731600306177"
        ],
        "id": "1602153731600306177",
        "text": "RT @griteater: OK I've seen enough to say that I'm bullish on a solid cold period E of the Rockies to Deep South just before Christmas thru…"
        },
        {
        "edit_history_tweet_ids": [
            "1602153612603334656"
        ],
        "id": "1602153612603334656",
        "text": "@AndrewDevoss @WingDynasty @kelly_ques Seems Andy didn't appreciate the vid. This vid seems to have an excellent \"block rate\" reaction from libtard accounts. I'm going to be using it frequently: https://t.co/3az4zh3WSd"
        },
        {
        "edit_history_tweet_ids": [
            "1602153018564255747"
        ],
        "id": "1602153018564255747",
        "text": "@skipadeefarm @dirtvision @whiskeymyers @MaconCentreplex Amazing as always! Great video and sound and I feel almost like I'm there live!! Excellent coverage by @dirtvision"
        },
        {
        "edit_history_tweet_ids": [
            "1602152468917387268"
        ],
        "id": "1602152468917387268",
        "text": "RT @o_keilani: Gen Z is doing excellent and changing the landscape of what it means to be a professional 😭 they said to hell with everythin…"
        },
        {
        "edit_history_tweet_ids": [
            "1602152171168010240"
        ],
        "id": "1602152171168010240",
        "text": "I’m glad he isn’t rushing it tho I know he said he felt his albums were rushed I’m just desperate to listen to an excellent album https://t.co/UPkwXcxZ09"
        },
        {
        "edit_history_tweet_ids": [
            "1602155592650559489"
        ],
        "id": "1602155592650559489",
        "text": "Forgot to mention I filed for my LLC today. JK Dean &amp; Associates incoming. I feel like a proud parent 🥹🥹. Excuse me for a sec, I’m going to stare into my mirror and tell myself words of affirmation."
        },
        {
        "edit_history_tweet_ids": [
            "1602155590175887360"
        ],
        "id": "1602155590175887360",
        "text": "RT @lathamlawsnance: @ScoutSteveR This made me teary eyed, not to proud to admit that. https://t.co/uUMpqFJCir"
        },
        {
        "edit_history_tweet_ids": [
            "1602155581099446272"
        ],
        "id": "1602155581099446272",
        "text": "RT @Im__Soniiii: Hey @ishehnaaz_gill you are such a strong girl. You taught me how to fight when life gets too difficult to bear.I really p…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155573491159040"
        ],
        "id": "1602155573491159040",
        "text": "RT @joydipa_chy: You know what?! I was not ever so proud of this month unless I became one of these craziest fans of urs! I still brag arou…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155570705866752"
        ],
        "id": "1602155570705866752",
        "text": "RT @bleghstie: the motionless in white looks i did this year helped me push my creativity more than i ever have before, and i’m so proud of…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155554025410560"
        ],
        "id": "1602155554025410560",
        "text": "Also one thing that I noticed since I came here is actually there are still some discrimination here w there undermined which is same as Japan. Cuz they sometimes treat differently I thought. It of course depends on the person tho… but I’m so proud of me that I’m from Japan❤️‍🔥"
        },
        {
        "edit_history_tweet_ids": [
            "1602155553492729856"
        ],
        "id": "1602155553492729856",
        "text": "The way I been cutting ties lately… im proud of me. It was way past due"
        },
        {
        "edit_history_tweet_ids": [
            "1602155551202361345"
        ],
        "id": "1602155551202361345",
        "text": "RT @lathamlawsnance: @ScoutSteveR This made me teary eyed, not to proud to admit that. https://t.co/uUMpqFJCir"
        },
        {
        "edit_history_tweet_ids": [
            "1602155516612022274"
        ],
        "id": "1602155516612022274",
        "text": "I’m proud of me this semester 😌"
        },
        {
        "edit_history_tweet_ids": [
            "1602155505039724544"
        ],
        "id": "1602155505039724544",
        "text": "RT @lathamlawsnance: @ScoutSteveR This made me teary eyed, not to proud to admit that. https://t.co/uUMpqFJCir"
        },
        {
        "edit_history_tweet_ids": [
            "1602155471246626817"
        ],
        "id": "1602155471246626817",
        "text": "RT @jesus_really_: I was so proud of myself for taking his big ass dick 🤤🤤🤤 watch me take big dicks like this one @ https://t.co/LAOnLU6Yv2…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155466720690176"
        ],
        "id": "1602155466720690176",
        "text": "RT @heartstperxjoe: joe locke presenting at the emmys while being an emmy nominee himself for his first acting role after less than 8 month…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155449368936448"
        ],
        "id": "1602155449368936448",
        "text": "RT @Im__Soniiii: Hey @ishehnaaz_gill you are such a strong girl. You taught me how to fight when life gets too difficult to bear.I really p…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155442494488576"
        ],
        "id": "1602155442494488576",
        "text": "RT @lathamlawsnance: @ScoutSteveR This made me teary eyed, not to proud to admit that. https://t.co/uUMpqFJCir"
        },
        {
        "edit_history_tweet_ids": [
            "1602155436052213760"
        ],
        "id": "1602155436052213760",
        "text": "@iimaney it took me few seconds to recognize you sjjsjs. yes we are all so proud❤️"
        },
        {
        "edit_history_tweet_ids": [
            "1602155415176896512"
        ],
        "id": "1602155415176896512",
        "text": "RT @lathamlawsnance: @ScoutSteveR This made me teary eyed, not to proud to admit that. https://t.co/uUMpqFJCir"
        },
        {
        "edit_history_tweet_ids": [
            "1602155411825573889"
        ],
        "id": "1602155411825573889",
        "text": "RT @ajeebdastaan_: Pranali Rathod, an ITA award winner at 23. I AM SO EMOTIONAL 😭🤍 it takes me back to the days when she was passed off and…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155382851325953"
        ],
        "id": "1602155382851325953",
        "text": "RT @Im__Soniiii: Hey @ishehnaaz_gill you are such a strong girl. You taught me how to fight when life gets too difficult to bear.I really p…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155312404135936"
        ],
        "id": "1602155312404135936",
        "text": "RT @Freedom16356531: #PrinceWilliam said “I wouldn’t let it break me, I wanted it to make me. I wanted her to be proud of the person I’d be…"
        },
        {
        "edit_history_tweet_ids": [
            "1602155282548723712"
        ],
        "id": "1602155282548723712",
        "text": "RT @joydipa_chy: You know what?! I was not ever so proud of this month unless I became one of these craziest fans of urs! I still brag arou…"
        },
        {
        "edit_history_tweet_ids": [
            "1601628054388105216"
        ],
        "id": "1601628054388105216",
        "text": "An American rapper's money show.jpg \nhttps://t.co/S2mgqaeUGG \n\nA rapper named Kodak Black is on the ... \n#bragging #rapper #theUnitedStates \nhttps://t.co/S2mgqaeUGG"
        },
        {
        "edit_history_tweet_ids": [
            "1601497474497069056"
        ],
        "id": "1601497474497069056",
        "text": "⭐️Bragging Rights⭐️\n\nA couple of the many products available in this print.\n\nhttps://t.co/h9lFrr2EAq \n\n#bragging #hotdogs #sale #gift #shoppingonline #food #shopping #onlineshopping https://t.co/SVhT3Byly4"
        },
        {
        "edit_history_tweet_ids": [
            "1601497367324131328"
        ],
        "id": "1601497367324131328",
        "text": "⭐️Bragging Rights⭐️\n\nA couple of the many products available in this print.\n\nhttps://t.co/CcjeuIm39S \n\n#bragging #hotdogs #sale #gift #shoppingonline #food #shopping #onlineshopping https://t.co/fNBmIAhrWQ"
        },
        {
        "edit_history_tweet_ids": [
            "1600843638434578433"
        ],
        "id": "1600843638434578433",
        "text": "This word is most likely a combination of braggart and the Italian suffix occhio, related to the word for eye. Pretty easy to see in others, hard to realise it for one's self.\n\n#funwithwords #bragging #braggart #braggadocio #wotd #kwhungryminds https://t.co/u5hMpFpxJV"
        },
        {
        "edit_history_tweet_ids": [
            "1600667423140552704"
        ],
        "id": "1600667423140552704",
        "text": "RT @Dean_Devlin: Yup! #Bragging #LeverageRedemption @AmazonFreevee https://t.co/hf9ZhtJkmz"
        },
        {
        "edit_history_tweet_ids": [
            "1600633200715468800"
        ],
        "id": "1600633200715468800",
        "text": "#bragging on some of our @brewerhighwsisd Life Skills Ss. They worked cooperatively to prepare a holiday meal to share. I was excited to see the #pride they took in their accomplishment. Thank you to the Ts that helped #makeithappen! https://t.co/nv0MJxFb4G"
        },
        {
        "edit_history_tweet_ids": [
            "1600525899967135745"
        ],
        "id": "1600525899967135745",
        "text": "RT @Dean_Devlin: Yup! #Bragging #LeverageRedemption @AmazonFreevee https://t.co/hf9ZhtJkmz"
        },
        {
        "edit_history_tweet_ids": [
            "1600520431202713600"
        ],
        "id": "1600520431202713600",
        "text": "RT @Dean_Devlin: Yup! #Bragging #LeverageRedemption @AmazonFreevee https://t.co/hf9ZhtJkmz"
        },
        {
        "edit_history_tweet_ids": [
            "1600519057886806018"
        ],
        "id": "1600519057886806018",
        "text": "RT @Dean_Devlin: Yup! #Bragging #LeverageRedemption @AmazonFreevee https://t.co/hf9ZhtJkmz"
        },
        {
        "edit_history_tweet_ids": [
            "1600497359032668161"
        ],
        "id": "1600497359032668161",
        "text": "RT @Dean_Devlin: Yup! #Bragging #LeverageRedemption @AmazonFreevee https://t.co/hf9ZhtJkmz"
        },
        {
        "edit_history_tweet_ids": [
            "1600476580886679552"
        ],
        "id": "1600476580886679552",
        "text": "RT @Dean_Devlin: Yup! #Bragging #LeverageRedemption @AmazonFreevee https://t.co/hf9ZhtJkmz"
        },
        {
        "edit_history_tweet_ids": [
            "1600475567421546503"
        ],
        "id": "1600475567421546503",
        "text": "RT @Dean_Devlin: Yup! #Bragging #LeverageRedemption @AmazonFreevee https://t.co/hf9ZhtJkmz"
        },
        {
        "edit_history_tweet_ids": [
            "1600439320090841088"
        ],
        "id": "1600439320090841088",
        "text": "RT @Dean_Devlin: Yup! #Bragging #LeverageRedemption @AmazonFreevee https://t.co/hf9ZhtJkmz"
        },
        {
        "edit_history_tweet_ids": [
            "1600388181278412800"
        ],
        "id": "1600388181278412800",
        "text": "RT @Dean_Devlin: Yup! #Bragging #LeverageRedemption @AmazonFreevee https://t.co/hf9ZhtJkmz"
        },
        {
        "edit_history_tweet_ids": [
            "1600378248382119936"
        ],
        "id": "1600378248382119936",
        "text": "RT @Dean_Devlin: Yup! #Bragging #LeverageRedemption @AmazonFreevee https://t.co/hf9ZhtJkmz"
        },
        {
        "edit_history_tweet_ids": [
            "1600354034539409408"
        ],
        "id": "1600354034539409408",
        "text": "RT @Dean_Devlin: Yup! #Bragging #LeverageRedemption @AmazonFreevee https://t.co/hf9ZhtJkmz"
        },
        {
        "edit_history_tweet_ids": [
            "1600304942631092224"
        ],
        "id": "1600304942631092224",
        "text": "RT @Dean_Devlin: Yup! #Bragging #LeverageRedemption @AmazonFreevee https://t.co/hf9ZhtJkmz"
        },
        {
        "edit_history_tweet_ids": [
            "1600301837063634944"
        ],
        "id": "1600301837063634944",
        "text": "RT @Dean_Devlin: Yup! #Bragging #LeverageRedemption @AmazonFreevee https://t.co/hf9ZhtJkmz"
        },
        {
        "edit_history_tweet_ids": [
            "1600298907262586880"
        ],
        "id": "1600298907262586880",
        "text": "RT @Dean_Devlin: Yup! #Bragging #LeverageRedemption @AmazonFreevee https://t.co/hf9ZhtJkmz"
        },
        {
        "edit_history_tweet_ids": [
            "1600297865955356672"
        ],
        "id": "1600297865955356672",
        "text": "RT @Dean_Devlin: Yup! #Bragging #LeverageRedemption @AmazonFreevee https://t.co/hf9ZhtJkmz"
        }
    ]