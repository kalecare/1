# Save and run this Python script to generate the HTML file
html_template = """<!DOCTYPE html>
<html>
<head>
    <title>Python-Generated Live Graph</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body { background: #111; color: #fff; font-family: sans-serif; text-align: center; padding: 20px; }
        .container { max-width: 700px; margin: 0 auto; background: #222; padding: 20px; border-radius: 12px; }
    </style>
</head>
<body>

<div class="container">
    <h2>Live Graph Stream (1 - 10)</h2>
    <canvas id="chart"></canvas>
</div>

<script>
    const ctx = document.getElementById('chart').getContext('2d');
    const chart = new Chart(ctx, {
        type: 'line',
        data: { labels: [], datasets: [{ label: 'Value', data: [], borderColor: '#00ff88', tension: 0.3 }] },
        options: { scales: { y: { min: 1, max: 10 } } }
    });

    let sec = 0;
    setInterval(() => {
        sec++;
        const val = Math.floor(Math.random() * 10) + 1;
        chart.data.labels.push(sec + 's');
        chart.data.datasets[0].data.push(val);
        
        if (chart.data.labels.length > 15) {
            chart.data.labels.shift();
            chart.data.datasets[0].data.shift();
        }
        chart.update();
    }, 1000);
</script>
</body>
</html>
"""

with open("live_graph.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("Generated live_graph.html successfully!")