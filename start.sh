if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/PrinceStarLord/Nazriya2
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Nazriya2
fi
cd /Nazriya2
pip3 install -U -r requirements.txt
echo "Starting Bot..."
python3 bot.py
