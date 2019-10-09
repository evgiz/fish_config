# Greeting
function fish_greeting 
    clear
    printf '\e[3J'
    set_color yellow
    echo " ______ _____  _____ _    _ 
|  ____|_   _|/ ____| |  | |
| |__    | | | (___ | |__| |
|  __|   | |  \___ \|  __  |
| |     _| |_ ____) | |  | |
|_|    |_____|_____/|_|  |_|
"
    set_color normal
end

# Real clear
function new
    source $__fish_config_dir/config.fish
    fish_greeting
end

# Quick tmp
function tmp
    cd $HOME/Development/.tmp
    set -lx TMP_PATH_NAME (date +"%d-%m-%Y_%T")
    mkdir $TMP_PATH_NAME
    cd $TMP_PATH_NAME
    set_color yellow
    echo "Created temporary directory "$TMP_PATH_NAME
    set_color normal
end

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
abbr -a -g gclone git clone

# Github
function ghclone 
    git clone "http://github.com/evgiz/"$argv[1] $argv[2]
end

# Destinations
abbr -a -g fishy $__fish_config_dir
abbr -a -g desk $HOME/Desktop/
abbr -a -g samf $HOME/Development/Samfundet/Samfundet
abbr -a -g home cd

function dev
    cd $HOME/Development
    ls 
end

function stud
    cd $HOME/Studies
    ls 
end

# Python
abbr -a -g py python3
abbr -a -g pip pip3
abbr -a -g py2 python
abbr -a -g pip2 pip

# Python scripts manager
abbr -a -g mypys mypy -l
function mypy 
    if test (count $argv) = 0
        set_color yellow
        echo 'Usage: mypy <name>'
        set_color normal        
    else if test $argv[1] = "-h"
        set_color green
        echo "  Usage"
        set_color yellow
        echo '  run     mypy <name>'
        echo '  add     mypy -a <file>'
        echo '  new     mypy -n <name>'
        echo '  edit    mypy -e <name>'
        echo '  rename  mypy -r <name> <new_name>'
        echo '  open    mypy -o'
        echo '  list    mypy -l'
        set_color normal
    else if test $argv[1] = "-l"
        if test -e $__fish_config_dir/mypy/".list.py"
            python3 $__fish_config_dir/mypy/".list.py"
        else
            set_color green
            echo '-------------------------'
            set_color red
            ls $__fish_config_dir/mypy
            set_color green
            echo '-------------------------'
            set_color normal
        end
    else if test $argv[1] = "-e"
        if test (count $argv) = 2
            if test -e $__fish_config_dir/mypy/$argv[2]".py"
                code $__fish_config_dir/mypy/$argv[2]".py"
                set_color green
                echo "Script opened in code."
                set_color normal
            else
                set_color red
                echo "File not found."
                set_color normal
            end
        else
            set_color yellow
            echo "Usage: mypy -e <name>"
            set_color normal
        end
    else if test $argv[1] = "-a"
        if test (count $argv) = 2
            if test -e $argv[2]
                if test -e $__fish_config_dir/mypy/$argv[2]
                    set_color red
                    echo "Name already in use."
                    set_color normal
                else
                    cp $argv[2] $__fish_config_dir/mypy/
                    set_color green
                    echo "Script added to mypys."
                    set_color normal
                end
            else
                set_color red
                echo "File not found."
                set_color normal
            end
        else
            set_color yellow
            echo "Usage: mypy -a <file>"
            set_color normal
        end
    else if test $argv[1] = "-n"
        if test (count $argv) = 2
            if test -e $__fish_config_dir/mypy/$argv[2]".py"
                set_color red
                echo "Name already exists."
                set_color normal
            else
                touch $__fish_config_dir/mypy/$argv[2]".py"
                set_color green
                echo "Created new mypy script."
                set_color normal
                code $__fish_config_dir/mypy/$argv[2]".py"
            end
        else
            set_color yellow
            echo "Usage: mypy -n <name>"
            set_color normal
        end
    else if test $argv[1] = "-r"
        if test (count $argv) = 3
            if test -e $__fish_config_dir/mypy/$argv[2]".py"
                if test -e $__fish_config_dir/mypy/$argv[3]".py"
                    set_color red
                    echo "Name already exists."
                    set_color normal
                else
                    mv $__fish_config_dir/mypy/$argv[2]".py" $__fish_config_dir/mypy/$argv[3]".py"
                    set_color green
                    echo "Renamed script."
                    set_color normal
                end
            else
                set_color red
                echo "Script not found."
                set_color normal
            end
        else
            set_color yellow
            echo "Usage: mypy -r <name> <new_name>"
            set_color normal
        end
    else if test $argv[1] = "-o"
        open $__fish_config_dir/mypy/
    else
        if test -e $__fish_config_dir/mypy/$argv[1]".py"
            python3 $__fish_config_dir/mypy/$argv[1]".py" $argv[2..-1]
        else
            set_color red
            echo "Script not found."
            set_color normal
        end
    end
end

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
