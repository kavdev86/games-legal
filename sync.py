"""Copy the legal pages from the game projects: python sync.py, then commit and push."""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
GAMES = {
    'ataka-zombi': r'E:\my\WalkersAttack\public',
    'orda': r'E:\my\Orda\public',
    # Башня Тихого Мастера: не public/ — оттуда страницы уехали бы в сборки игры.
    'silent-tower': r'E:\my\NeuroFlask-0.11.2\docs\legal',
}

for folder, src in GAMES.items():
    os.makedirs(os.path.join(HERE, folder), exist_ok=True)
    for name in ('privacy.html', 'terms.html'):
        shutil.copyfile(os.path.join(src, name), os.path.join(HERE, folder, name))
        print(folder, name)
