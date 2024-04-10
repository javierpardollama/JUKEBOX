from services.shell_service import ShellService


shellService = ShellService()

try:
    shellService.start()
except KeyboardInterrupt:
    print('Interrumpiendo')
try:
    shellService.stop()
except SystemExit:
    shellService.stop()
