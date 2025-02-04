import os
import ctypes
from ctypes import wintypes

class DesktopIconManager:
    def __init__(self):
        self.desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

    def get_icons(self):
        icons = [f for f in os.listdir(self.desktop_path) if f.endswith('.lnk') or os.path.isdir(os.path.join(self.desktop_path, f))]
        return icons

    def arrange_icons(self, arrangement_type='grid'):
        # This is a placeholder for arranging icons logic
        # Currently just prints the available icons
        icons = self.get_icons()
        if arrangement_type == 'grid':
            print("Arranging icons in grid format:")
        elif arrangement_type == 'list':
            print("Arranging icons in list format:")
        else:
            print(f"Unknown arrangement type: {arrangement_type}")

        for icon in icons:
            print(f" - {icon}")

    def refresh_desktop(self):
        # Refresh the desktop programmatically
        ctypes.windll.user32.SystemParametersInfoW(0x0014, 0, None, 0)

def main():
    manager = DesktopIconManager()
    print("Available icons on desktop:")
    icons = manager.get_icons()
    for icon in icons:
        print(f" - {icon}")

    manager.arrange_icons(arrangement_type='grid')
    manager.refresh_desktop()
    print("Desktop refreshed.")

if __name__ == "__main__":
    main()