import PySimpleGUI as sg

def mode_1_layout():
    return [
        [sg.Text('Pose Detection Mode 1')],
        [sg.Button('Start Mode 1')],
        [sg.Button('Return')]
    ]

def mode_2_layout():
    return [
        [sg.Text('Pose Detection Mode 2')],
        [sg.Button('Start Mode 2')],
        [sg.Button('Return')]
    ]

def main_layout():
    return [
        [sg.Text('Main Page')],
        [sg.Button('Mode 1')],
        [sg.Button('Mode 2')]
    ]

def mode_1():
    window = sg.Window('Pose Detection Mode 1', mode_1_layout(), finalize=True, element_justification='c', size=(400,300))

    while True:
        event, _ = window.read(timeout=100)  # Check for events every 100 milliseconds
        print('Mode 1 running...')  # Print continuously while in Mode 1

        if event == sg.WINDOW_CLOSED:
            break

        if event == 'Start Mode 1':
            print('Mode 1 started...')

        elif event == 'Return':
            print("Returning to Main Menu.")
            window.close()
            return

    window.close()


def mode_2():
    window = sg.Window('Pose Detection Mode 2', mode_2_layout(), finalize=True, element_justification='c', size=(400,300))

    while True:
        event, _ = window.read(timeout=100)  # Check for events every 100 milliseconds
        print('Mode 2 running...')  # Print continuously while in Mode 2

        if event == sg.WINDOW_CLOSED:
            break

        if event == 'Start Mode 2':
            print('Mode 2 started...')

        elif event == 'Return':
            print("Returning to Main Menu.")
            window.close()
            return

    window.close()


def main():
    sg.theme('Default1')

    main_window = sg.Window('Pose Detection - Main Menu', main_layout(), finalize=True, element_justification='c', size=(400,300))

    while True:
        event, _ = main_window.read()

        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break

        if event == 'Mode 1':
            main_window.hide()
            mode_1()
            main_window.un_hide()

        elif event == 'Mode 2':
            main_window.hide()
            mode_2()
            main_window.un_hide()

    main_window.close()

if __name__ == '__main__':
    main()
