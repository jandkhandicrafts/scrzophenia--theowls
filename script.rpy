# Characters and Images
image hacker_room = "hacker_room.png"
image city_outside = "city_outside.png"
image psych_ward = "psych_ward.png"
image glitch = "glitch_overlay.png"
image memory_fragment = "memory_fragment.png"
image virus = "virus_overlay.png"
image elior = "elior.png"
image cipher = "cipher.png"
image ashen = "ashen.png"

define e = Character("Elior", color="#8888ff")
define c = Character("Cipher", color="#aaffaa")
define a = Character("Ashen", color="#ff8888")
define ghost = Character("Ghost", color="#ff00ff")
define n = Character(None)

default cipher_alive = True
default ashen_alive = True
default memory_lost = False

label start:
    play music "bgm_main_theme.ogg" fadein 1.5

    scene hacker_room with fade
    show cipher at left
    show elior at center
    show ashen at right
    n "The hacker room is bathed in the cold glow of multiple monitors. City lights flicker outside the window."
    e "Everything's ready."
    c "All systems are primed. We go in on your mark, Elior."
    a "Stay sharp. Once we're inside, there's no turning back."
    e "(This could be the one chance. I can hear the code pulsing like a heartbeat in the circuitry.)"
    n "Without warning, the monitors briefly distort with static."
    show glitch with dissolve
    pause 0.5
    hide glitch
    n "A distorted voice crackles through the speakers, barely human."
    ghost "\"You have come far, little fire... But all roads end here. Sacrifice is required.\""
    e "(This is it. The ghost demands payment for passage.)"
    a "Elior... what do we do?"
    c "The AI is more than a program. It's demanding a toll."
    ghost "\"I will let the path clear only if you give me what I want.\""

    menu:
        "Sacrifice Cipher to appease the ghost.":
            $ cipher_alive = False
            jump sacrifice_cipher
        "Sacrifice Ashen to appease the ghost.":
            $ ashen_alive = False
            jump sacrifice_ashen
        "Sacrifice one of Elior's memories.":
            $ memory_lost = True
            jump sacrifice_memory
        "Refuse to sacrifice anyone.":
            jump refuse_sacrifice

label sacrifice_cipher:
    e "Cipher... I'm so sorry."
    c "Elior... I trust you."
    e "(Cold logic overrode every other instinct. I never imagined trusting this decision.)"
    show glitch with hpunch
    pause 0.3
    hide glitch
    ghost "\"You have chosen... proceed.\""
    a "(Ashen says nothing. His face is tight, unreadable.)"
    e "(Cipher didn't plead or panic. In the back of my mind, I wonder if I made a terrible mistake.)"
    hide cipher
    jump after_first_choice

label sacrifice_ashen:
    e "Ashen..."
    a "I made my choice when I joined you. Go. The rest of us depend on it."
    e "(He doesn't show fear. It's as if he's already at peace.)"
    show glitch with hpunch
    pause 0.3
    hide glitch
    ghost "\"You have chosen... proceed.\""
    c "(Cipher stands motionless, shock flickering in her eyes.)"
    e "(Her silence weighs heavier than words.)"
    hide ashen
    jump after_first_choice

label sacrifice_memory:
    e "Take my memories... I will forget it all to make this right."
    show memory_fragment with dissolve
    pause 1.0
    hide memory_fragment
    ghost "\"You have given much... proceed.\""
    c "He lost a piece of himself without hesitation."
    a "The cost was his own past."
    e "(An emptiness lingers where memories once were. The ghost's voice fades, but a hollow ache remains.)"
    jump after_first_choice

label refuse_sacrifice:
    e "No. I won't sacrifice my team. There has to be another way."
    ghost "\"Your pride will be your undoing... very well.\""
    c "This might be a trap, Elior."
    a "He’s pissed. We shouldn’t keep pushing without an edge."
    e "(Doubt creeps in. Was there really another path?)"
    jump after_first_choice

label after_first_choice:
    show virus with dissolve
    pause 0.5
    hide virus
    n "The digital storm intensifies. Code streams warp across the screens."
    if not cipher_alive and not ashen_alive:
        n "The room falls silent as both allies vanish into the digital haze..."
    elif not cipher_alive:
        a "We lost Cipher... but we have to keep going."
    elif not ashen_alive:
        c "Ashen is gone... but we proceed."
    elif memory_lost:
        n "Elior’s eyes flicker with uncertainty. Something important is missing."
    else:
        n "Both allies stand tense. The code pulsing feels like a ticking clock."
    e "(No matter the cost, I have to push forward. There's no turning back now.)"
    show glitch with dissolve
    pause 0.2
    hide glitch
    n "The ghost speaks again through the static."
    ghost "\"Another toll awaits. You still must pay it.\""
    e "(They want more sacrifice. How much is enough?)"
    jump second_choice

label second_choice:
    if not cipher_alive and not ashen_alive:
        jump end_branch
    if memory_lost == False:
        if cipher_alive and ashen_alive:
            menu:
                "Sacrifice Cipher.":
                    $ cipher_alive = False
                    jump sacrifice_cipher_2
                "Sacrifice Ashen.":
                    $ ashen_alive = False
                    jump sacrifice_ashen_2
                "Sacrifice another memory.":
                    $ memory_lost = True
                    jump sacrifice_memory_2
                "Continue without sacrifice.":
                    jump continue_second
        elif cipher_alive:
            menu:
                "Sacrifice Cipher.":
                    $ cipher_alive = False
                    jump sacrifice_cipher_2
                "Sacrifice another memory.":
                    $ memory_lost = True
                    jump sacrifice_memory_2
                "Continue without sacrifice.":
                    jump continue_second
        elif ashen_alive:
            menu:
                "Sacrifice Ashen.":
                    $ ashen_alive = False
                    jump sacrifice_ashen_2
                "Sacrifice another memory.":
                    $ memory_lost = True
                    jump sacrifice_memory_2
                "Continue without sacrifice.":
                    jump continue_second
    else:
        if cipher_alive and ashen_alive:
            menu:
                "Sacrifice Cipher.":
                    $ cipher_alive = False
                    jump sacrifice_cipher_2
                "Sacrifice Ashen.":
                    $ ashen_alive = False
                    jump sacrifice_ashen_2
                "Continue without sacrifice.":
                    jump continue_second
        elif cipher_alive:
            menu:
                "Sacrifice Cipher.":
                    $ cipher_alive = False
                    jump sacrifice_cipher_2
                "Continue without sacrifice.":
                    jump continue_second
        elif ashen_alive:
            menu:
                "Sacrifice Ashen.":
                    $ ashen_alive = False
                    jump sacrifice_ashen_2
                "Continue without sacrifice.":
                    jump continue_second

label sacrifice_cipher_2:
    e "Cipher..."
    c "I won't let you down."
    show glitch with hpunch
    pause 0.3
    hide glitch
    ghost "\"You are emptying your hands... proceed.\""
    if ashen_alive:
        a "We move on without her. For the mission."
    e "(Ashen’s gaze is steady. His loyalty never wavers, even after so much loss.)"
    hide cipher
    jump end_branch

label sacrifice_ashen_2:
    e "Ashen..."
    a "It ends with me. Go now."
    show glitch with hpunch
    pause 0.3
    hide glitch
    ghost "\"You accept oblivion. Proceed.\""
    if cipher_alive:
        c "Without him, we endure... together."
    e "(Cipher’s resolve steadies me. We face what comes.)"
    hide ashen
    jump end_branch

label sacrifice_memory_2:
    e "Another memory... take it."
    show memory_fragment with dissolve
    pause 1.0
    hide memory_fragment
    ghost "\"Your mind shall be mine. Proceed...\""
    if cipher_alive and ashen_alive:
        c "His past is fading, bit by bit."
        a "We're losing pieces of him."
    elif cipher_alive:
        c "He's sacrificing his very mind now."
    elif ashen_alive:
        a "The sacrifice cuts deep into his mind."
    e "(Each fragment lost leaves a void. I barely recognize myself.)"
    jump end_branch

label continue_second:
    e "No more. Whatever you want, we won't give it."
    ghost "\"Foolish. Your reality will fracture...\""
    if cipher_alive and ashen_alive:
        c "Keep pushing, Elior."
        a "We'll handle the rest."
    elif cipher_alive:
        c "I'm here. You can do this."
    elif ashen_alive:
        a "You have my back, Elior."
    e "(My vision blurs; the world warps around me.)"
    show glitch with dissolve
    pause 0.5
    hide glitch
    jump end_branch

label end_branch:
    if not cipher_alive and not ashen_alive:
        jump ending_psych
    elif memory_lost:
        jump ending_haunting
    else:
        jump ending_surreal

label ending_psych:
    scene psych_ward with fade
    n "A sharp white light. Beeping monitors. You awaken strapped to a hospital bed."
    n "An IV drip in your arm, and nothing but the sterile hum of a psych ward around you."
    e "(Memories are fragments... were the hackers ever real?)"
    ghost "\"All companions lost... your mind is mine now.\""
    n "A figure looms in your peripheral vision – familiar yet alien."
    ghost "\"Say goodnight, Elior.\""
    n "As everything fades, you realize the ghost was never in the circuit, but in your mind."
    n "END."
    menu:
        "Restart the game.":
            jump start
        "Quit.":
            return

label ending_haunting:
    scene city_outside with fade
    if cipher_alive or ashen_alive:
        n "You stand beneath the city's neon haze, alone among the digital night. Memories have been traded for this silence."
    else:
        n "The world feels thinner, haunted by what you lost."
    e "(The echoes of ghosts — and lost memories — linger.)"
    ghost "\"Did you find what you were looking for? Or did you lose yourself instead?\""
    n "The lines between reality and code blur as the ghost watches you from the shadows."
    n "END."
    menu:
        "Restart the game.":
            jump start
        "Quit.":
            return

label ending_surreal:
    scene hacker_room with fade
    show glitch with dissolve
    n "The room tilts and shudders, pixels bleeding out from the monitors."
    if cipher_alive and ashen_alive:
        n "Neither ally was sacrificed, but nothing is as it seems."
    else:
        n "Reality twists and fractures, despite having no memory lost."
    e "(My hands hover over the keyboard... but the code flows like liquid in the air.)"
    show virus with dissolve
    pause 0.5
    hide virus
    ghost "\"Congratulations... Your reality is now mine.\""
    n "Elior is adrift between worlds – a ghost in the machine, forever uncertain of what is real."
    n "END."
    menu:
        "Restart the game.":
            jump start
        "Quit.":
            return
