import androidhelper

droid = androidhelper.Android()


title=("Crazy Little Thing Called Love")

content=("This thing called love \n I just can't handle it \n This thing called love \n I must get round to it \n I ain't ready \n Crazy little thing called love \n \n This thing (this thing) called love (called love) \nIt cries (like a baby) \n In a cradle all night \n It swings (woo woo) \n It jives (woo woo) \n It shakes all over like a jelly fish \n I kinda like it \n Crazy little thing called love \n \n There goes my baby \n She knows how to rock'n'roll \n She drives me crazy \n \n She gives me hot and cold fever \n She leaves me in a cool cool sweat \n \n I gotta be cool, relax, get hip! \n Get on my track's \n Take a back seat \n Hitchhike \n And take a long ride on my motor bike \n Until I'm ready \n Crazy little thing called love \n \n I gotta be cool, relax, get hip! \n Get on my track's \n Take a back seat \n Hitchhike \n And take a long ride on my motor bike \n Until I'm ready (ready, Freddie) \n Crazy little thing called love \n \n This thing called love \n I just can't handle it \n This thing called love \n I must get round to it \n I ain't ready \n Crazy little thing called love \n Crazy little thing called love, yeah, yeah \n \n Crazy little thing called love, yeah, yeah \n Crazy little thing called love, yeah, yeah \n Crazy little thing called love, yeah, yeah \n Crazy little thing called love, yeah, yeah \n Crazy little thing called love, yeah, yeah \n Crazy little thing called love, yeah, yeah \n Crazy little thing called love, yeah, yeah.")

msg = 'Você deseja visualizar a letra da música: \nCrazy Little Thing Called Love?'
title = 'www.letras.mus.br/queen/76864/'

droid.dialogCreateAlert(title, msg)

droid.dialogSetPositiveButtonText('Sim')
droid.dialogSetNegativeButtonText('Nao')
droid.dialogSetNeutralButtonText('Cancela')

droid.dialogShow()

botao = droid.dialogGetResponse().result

if botao['which'] == 'positive':
    droid.dialogCreateAlert(title, content)
elif botao['which'] == 'negative':
    droid.makeToast('Ok!')

droid.dialogShow()