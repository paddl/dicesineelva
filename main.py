def on_gesture_logo_up():
    basic.show_number(randint(7, 12))
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_button_pressed_a():
    basic.show_icon(IconNames.DIAMOND)
    for index in range(2):
        music.play(music.string_playable("C5 B A G F E D C ", 120),
            music.PlaybackMode.UNTIL_DONE)
    basic.show_leds("""
        # # # # #
        # . # . #
        # # # # #
        # . # . #
        # . . . #
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_number(randint(1, 6))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_logo_down():
    basic.show_number(randint(13, 18))
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def on_button_pressed_b():
    basic.show_icon(IconNames.SMALL_DIAMOND)
    music.play(music.string_playable("C D G E C F A C5 ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("C D G E C F A C5 ", 151),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_leds("""
        # # # # #
        # # . # #
        # . # . #
        # . . . #
        # . . . #
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

images.create_big_image("""
    . . # . . # . . # .
    . # . # # . # # . #
    . . # . . # . . # .
    . . # . . # . . # .
    # # # # # # # # # #
    """).scroll_image(1, 200)
basic.pause(1000)
basic.clear_screen()