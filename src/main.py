class OpenCity:
    build = "0.00.000.0060"
    Version = "0.2"
    Premium = True
    Special_sandbox = True
    debug = False
    Name = "OpenCity"


__version__ = OpenCity.Version


if __name__ == '__main__':
    print("{} v{} \nBuild ({}) \n\n\n".format(OpenCity.Name, OpenCity.Version, OpenCity.build))
    # from files_and_folders import folder_and_file_creator as ft
    # from premium.premium_test import premium_test as pt
    # from special_sandbox.special_sandbox_mode_test import special_sandbox_mode_test as st
    import opencity_kivy.splashscreen as ss

    # ft()
    # print()
    # pt()
    # print()
    # st()
    # print()
    ss.OpenCityApp().run()