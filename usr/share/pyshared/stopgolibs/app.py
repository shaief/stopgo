import argparse
from sys import argv
import os
from os.path import expanduser
import wx

HOME = os.path.expanduser('~')

def getOptions():
    '''
    Analizu datumoj
    '''
    args = argv[1:]
    parser = argparse.ArgumentParser(description="Parses command.",argument_default=argparse.SUPPRESS)
    parser.add_argument("project",nargs="?")
    parser.add_argument("-c", "--config",nargs="?",dest='config',
                        help="Optional path to a non-default config file.")
    parser.add_argument("-s", "--shell",dest='shell',action='store_true',help="Keep it in the shell. Do not launch the GUI.")
    parser.add_argument("-m", "--make-project",nargs="?",dest='make',
                        help="Path to a directory of sequential images to load as if it were a StopGo project.")

    options = parser.parse_args(args)
    opts = vars(options)
    '''
    if not opts.has_key('project'):
        opts['project'] = 'stopgo_project.db'


    if not opts.has_key('config'):
        if os.path.isfile( os.path.join( HOME + '.config/stopgo.conf' ) ):
            opts['config'] = os.path.isfile( os.path.join( HOME + '/.config/stopgo.conf' ) ):
        elif os.path.isfile('/etc/config/stopgo.conf'):
            opts['config'] = '/etc/config/stopgo.conf'
        else:
            print('Failed: No template file found.')
            exit()
    '''

    if not opts.has_key('shell'):
        import gui
        gui.main(opts)
        #applo = wx.App()
        #instancer = gui.GUI(parent=None, id=-1, title="stopgo")
        #instancer.Show()
        #applo.MainLoop()
    else:
        import shell
        shell.execute(opts)
