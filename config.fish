# Greeting
set fish_greeting " ______ _____  _____ _    _ 
|  ____|_   _|/ ____| |  | |
| |__    | | | (___ | |__| |
|  __|   | |  \___ \|  __  |
| |     _| |_ ____) | |  | |
|_|    |_____|_____/|_|  |_|
"

# Git abbreviations
abbr -a -g g git
abbr -a -g ga git add
abbr -a -g gaa git add --all
abbr -a -g gcmsg git commit -m
abbr -a -g gc git commit -m
abbr -a -g gp git push
abbr -a -g gl git pull
abbr -a -g gst git status
abbr -a -g glog git log --oneline --decorate --color --graph
abbr -a -g gco git checkout
abbr -a -g gba git branch -a
abbr -a -g gb git branch
abbr -a -g gcm git checkout master
abbr -a -g gd git diff

# Destinations
abbr -a -g dev $HOME/Development/
abbr -a -g stud $HOME/Studies/
abbr -a -g desk $HOME/Desktop/
abbr -a -g samf $HOME/Development/Samfundet/Samfundet

# Python
abbr -a -g py python3
abbr -a -g pip pip3
abbr -a -g py2 python
abbr -a -g pip2 pip


# ==================== #
#  Applications (Mac)  #
# ==================== #

# VS Code
function code 
    if count $argv > /dev/null
        open $argv -a "/Applications/Visual Studio Code.app" 
    else
        open . -a "/Applications/Visual Studio Code.app"
    end
end

# PyCharm
function pycharm 
    if count $argv > /dev/null
        open $argv -a "/Applications/PyCharm CE.app" 
    else
        open . -a "/Applications/PyCharm CE.app"
    end
end

# RubyMine
function rubymine 
    if count $argv > /dev/null
        open $argv -a "/Applications/RubyMine.app" 
    else
        open . -a "/Applications/RubyMine.app"
    end
end

# CLion
function clion 
    if count $argv > /dev/null
        open $argv -a "/Applications/CLion.app" 
    else
        open . -a "/Applications/CLion.app"
    end
end

# Love2D
function love
 if count $argv > /dev/null
        open $argv -a "/Applications/love.app" 
    else
        open . -a "/Applications/love.app"
    end
end
