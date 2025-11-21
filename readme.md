database design:

authenticated users:
    id: {
        name: String,
        taps: {
            totalTaps: number,
            currentTapSreak: {
                tappedToday: bool,
                lastTap: date
                streakStart: date
                currentStreak: number
            },

            tapStreaks: [
                {
                    streakStart: date,
                    currentStreak: number
                },
                {
                    streakStart: date,
                    currentStreak: number
                },
            ]
        
        }
    }

