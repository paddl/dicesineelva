input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Diamond)
    for (let index = 0; index < 2; index++) {
        music.play(music.stringPlayable("C5 B A G F E D C ", 120), music.PlaybackMode.UntilDone)
    }
    basic.showLeds(`
        # # # # #
        # . # . #
        # # # # #
        # . # . #
        # . . . #
        `)
})
input.onGesture(Gesture.LogoUp, function () {
    basic.showNumber(randint(7, 12))
})
input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.SmallDiamond)
    music.play(music.stringPlayable("C D G E C F A C5 ", 120), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("C D G E C F A C5 ", 151), music.PlaybackMode.UntilDone)
    basic.showLeds(`
        # # # # #
        # # . # #
        # . # . #
        # . . . #
        # . . . #
        `)
})
input.onGesture(Gesture.Shake, function () {
    basic.showNumber(randint(1, 6))
})
input.onGesture(Gesture.LogoDown, function () {
    basic.showNumber(randint(13, 18))
})
images.createBigImage(`
    . . # . . # . . # .
    . # . # # . # # . #
    . . # . . # . . # .
    . . # . . # . . # .
    # # # # # # # # # #
    `).scrollImage(1, 200)
basic.pause(1000)
basic.clearScreen()
