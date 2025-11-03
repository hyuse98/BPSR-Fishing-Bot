class StatsTracker:
    def __init__(self):
        self.stats = {
            'cycles': 0,
            'fish_caught': 0,
            'rod_breaks': 0,
            'timeouts': 0
        }

    def increment(self, stat_name, value=1):
        if stat_name in self.stats:
            self.stats[stat_name] += value

    def show(self):
        print("\n" + "=" * 50)
        print("📊 ESTATÍSTICAS")
        print("=" * 50)
        for stat, value in self.stats.items():
            title = stat.replace('_', ' ').replace('cycles', 'Ciclos completados').capitalize()
            print(f"  {title}: {value}")
        print("=" * 50)