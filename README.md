# Learn Japanese in terminal

### Setup

Install vocage and utilities (`vs` for vocage-stat and `vsd` for vocage-stat-dir)
```bash
yay -S vocage
cp util/vs ~/.local/bin/vs
cp util/vsd ~/.local/bin/vsd
```

### Usage

1. To study new lesson
```bash
cd kanji
vocage -z 47.tsv
```

2. To revise learned lesson
```bash
cd kanji
vocage -z -s 46.tsv
```

3. Directory structure:

Each course is a directory.
Each lesson is a `.tsv` file.
To check progress of each course, use:
```bash
vsd *
```

To check progress of each lesson, use:
```
cd kanji
vs *
```
