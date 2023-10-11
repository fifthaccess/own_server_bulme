OPTIND=1
while getopts u:n:p: flag
do
    case "${flag}" in
        u) username=${OPTARG};;
        n) projectname=${OPTRAG};;
        p) path=${OPTARG};;
       
    esac
done

echo $username
#sudo mkdir  "${projectname}.git"
git init ${path}/${projectname}.git --bare
