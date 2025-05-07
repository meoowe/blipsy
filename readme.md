# 🐾 Blipsy — A Pomodoro Timer That Stares Into Your Soul

**Blipsy** is a terminal-based Pomodoro timer with an animated ASCII cat who silently judges your every move.  
Because staring into a void cat's eyes makes you more productive.

## ✨ Features

- ⏳ Focus & break cycles (Pomodoro-style)
- 🐱 ASCII animation that blinks while you work
- 🎨 Customizable durations & messages
- 🧘 Quiet mode for terminal monks (`--no-art`)
- 🔔 Bell when time’s up
- 📊 Progress bar using [rich](https://github.com/Textualize/rich) to answer “how much longer?”

## 📥 Installation

> _If someone knows how to do this **properly**, please tell me._  
Until then:

```bash
# Clone the repo
git clone https://github.com/meoowe/blipsy
cd blipsy

# Install dependencies
pip install rich typer

# Run it
python blipsy.py run
```

## 🧪 Usage

Blipsy uses [Typer](https://typer.tiangolo.com), so it comes with built-in help:

```bash
python blipsy.py --help
```

### 🎯 Real Pomodoro Mode

```bash
python blipsy.py run
```

- 4 cycles
- 25 minutes work
- 5 minute short breaks
- 15 minute long break

You can customize all of this:

```bash
python blipsy.py run --cycles 2 --focus-secs 1200 --short-break-secs 300 --long-break-secs 900
```

### 🐾 Demo Mode

Want to test the animation without waiting 25 minutes?

```bash
python blipsy.py demo
```

### 😶 Quiet Mode (No Animation)

```bash
python blipsy.py run --no-art
```

## 🌟 Like it?

If Blipsy helped you do literally anything — drop a ⭐ on the repo.  
Or tell a friend. Or post a screenshot.  