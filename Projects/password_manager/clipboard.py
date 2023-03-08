class Clipboard:
    def set(string: str):
        # if macos use pbcopy instead of clip
        import subprocess
        cmd = f'echo {string.strip()}|clip'
        subprocess.check_call(cmd, shell=True)

Clipboard.set("happy birthday")