"""
LOGICAL BRUTALISM :: PAYLOAD :: DASHBOARD TEMPLATE
Generated file contents for the `init dashboard` scaffold.

Author: Matheus Lacerda Ferreira
License: MIT
"""

DASHBOARD_HTML = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>System Dashboard :: Logical Brutalism</title>

  <!-- Absolute Typography -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Iosevka+Aile:wght@400;500;700&family=Iosevka:wght@400;700&display=swap" rel="stylesheet">

  <!-- HTMX & Alpine.js -->
  <script src="https://unpkg.com/htmx.org@1.9.10" integrity="sha384-D1Kt99CQMDuVetoL1lrYwg5t+9QdHe7NLX/SoJYkXDFfX37iInKRy5xLSi8nO7UC" crossorigin="anonymous"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        borderRadius: {
          none: '0',
          DEFAULT: '0',
        },
        boxShadow: {
          none: 'none',
          DEFAULT: 'none',
        },
        extend: {
          colors: {
            void: '#0A0A0A',
            amber: '#FFB000',
            'text-dim': '#888888',
            'border-dim': '#333333',
            white: '#FFFFFF',
          },
          fontFamily: {
            struct: ['Iosevka Aile', 'sans-serif'],
            code: ['Iosevka', 'monospace'],
          }
        }
      },
      corePlugins: {
        borderRadius: false,
        boxShadow: false,
        transitionProperty: false,
        transitionDuration: false,
        transitionTimingFunction: false,
        transitionDelay: false,
        animation: false,
      }
    }
  </script>
  <style type="text/tailwindcss">
    @layer base {
      *, *::before, *::after {
        border-radius: 0 !important;
        transition: none !important;
        animation: none !important;
        box-shadow: none !important;
      }
    }
  </style>
</head>
<body class="bg-void text-text-dim font-struct h-screen w-screen overflow-hidden flex flex-col">

  <!-- Top Header -->
  <header class="border-b border-border-dim px-4 py-2 flex justify-between items-center text-xs font-code uppercase tracking-widest shrink-0">
    <div class="flex items-center gap-6">
      <span class="text-white font-bold">LOGICAL BRUTALISM // CONTROL</span>
      <span class="text-amber">LATENCY: 14ms</span>
    </div>
    <div class="flex items-center gap-4">
      <span>ENV: <span class="text-white">PROD</span></span>
      <span class="text-border-dim">|</span>
      <span>SYS_TIME: <span x-data="{ time: new Date().toISOString() }" x-init="setInterval(() => time = new Date().toISOString(), 1000)" x-text="time"></span></span>
    </div>
  </header>

  <!-- Main Content Area -->
  <div class="flex flex-1 overflow-hidden">
    
    <!-- Left Column: KPIs and Table -->
    <main class="flex-1 flex flex-col border-r border-border-dim overflow-y-auto p-4 space-y-6">
      
      <!-- KPI Grid -->
      <section class="grid grid-cols-4 gap-4">
        <!-- Card 1 -->
        <div class="border border-border-dim p-3 flex flex-col justify-between">
          <span class="text-xs uppercase font-code tracking-widest">Active Nodes</span>
          <div class="mt-2 flex items-baseline justify-between">
            <span class="text-3xl text-white font-bold">1,024</span>
            <span class="text-amber text-xs font-code">+2.4%</span>
          </div>
        </div>
        <!-- Card 2 -->
        <div class="border border-border-dim p-3 flex flex-col justify-between">
          <span class="text-xs uppercase font-code tracking-widest">Heap Usage</span>
          <div class="mt-2 flex items-baseline justify-between">
            <span class="text-3xl text-white font-bold">8.4GB</span>
            <span class="text-amber text-xs font-code">-1.2%</span>
          </div>
        </div>
        <!-- Card 3 -->
        <div class="border border-border-dim p-3 flex flex-col justify-between">
          <span class="text-xs uppercase font-code tracking-widest">Network I/O</span>
          <div class="mt-2 flex items-baseline justify-between">
            <span class="text-3xl text-white font-bold">1.2TB</span>
            <span class="text-amber text-xs font-code">+14.1%</span>
          </div>
        </div>
        <!-- Card 4 -->
        <div class="border border-border-dim p-3 flex flex-col justify-between">
          <span class="text-xs uppercase font-code tracking-widest">Error Rate</span>
          <div class="mt-2 flex items-baseline justify-between">
            <span class="text-3xl text-white font-bold">0.04%</span>
            <span class="text-amber text-xs font-code">0.0%</span>
          </div>
        </div>
      </section>

      <!-- High-Density Table -->
      <section class="flex-1 flex flex-col">
        <header class="flex justify-between items-center mb-2 font-code text-xs uppercase tracking-widest">
          <span>Transaction Ledger</span>
          <div class="space-x-2">
            <button hx-get="/api/ledger?page=prev" hx-target="#ledger-body" hx-swap="outerHTML" class="px-2 py-1 border border-border-dim text-white hover:bg-border-dim">PREV</button>
            <button hx-get="/api/ledger?page=next" hx-target="#ledger-body" hx-swap="outerHTML" class="px-2 py-1 border border-border-dim text-white hover:bg-border-dim">NEXT</button>
          </div>
        </header>
        
        <div class="border border-border-dim flex-1 overflow-auto">
          <table class="w-full text-left text-xs font-code border-collapse">
            <thead class="sticky top-0 bg-void border-b border-border-dim">
              <tr>
                <th class="py-1 px-2 font-normal text-text-dim">TX_ID</th>
                <th class="py-1 px-2 font-normal text-text-dim">TIMESTAMP</th>
                <th class="py-1 px-2 font-normal text-text-dim">SOURCE</th>
                <th class="py-1 px-2 font-normal text-text-dim">STATUS</th>
                <th class="py-1 px-2 font-normal text-text-dim text-right">SIZE</th>
              </tr>
            </thead>
            <tbody id="ledger-body">
              <tr class="border-b border-border-dim">
                <td class="py-1 px-2 text-white">0x8F92...A1B2</td>
                <td class="py-1 px-2">2026-07-28T19:22:01Z</td>
                <td class="py-1 px-2">node-us-east-1</td>
                <td class="py-1 px-2 text-amber">COMMITTED</td>
                <td class="py-1 px-2 text-right">4.2KB</td>
              </tr>
              <tr class="border-b border-border-dim">
                <td class="py-1 px-2 text-white">0x4C21...9F0E</td>
                <td class="py-1 px-2">2026-07-28T19:22:00Z</td>
                <td class="py-1 px-2">node-eu-west-3</td>
                <td class="py-1 px-2 text-amber">COMMITTED</td>
                <td class="py-1 px-2 text-right">1.8KB</td>
              </tr>
              <tr class="border-b border-border-dim">
                <td class="py-1 px-2 text-white">0x1A77...B89C</td>
                <td class="py-1 px-2">2026-07-28T19:21:58Z</td>
                <td class="py-1 px-2">node-sa-east-1</td>
                <td class="py-1 px-2 text-white">PENDING</td>
                <td class="py-1 px-2 text-right">8.1KB</td>
              </tr>
              <tr class="border-b border-border-dim">
                <td class="py-1 px-2 text-white">0x992B...33DF</td>
                <td class="py-1 px-2">2026-07-28T19:21:55Z</td>
                <td class="py-1 px-2">node-ap-south-1</td>
                <td class="py-1 px-2 text-amber">COMMITTED</td>
                <td class="py-1 px-2 text-right">2.0KB</td>
              </tr>
              <tr class="border-b border-border-dim">
                <td class="py-1 px-2 text-white">0x3E11...7A6D</td>
                <td class="py-1 px-2">2026-07-28T19:21:52Z</td>
                <td class="py-1 px-2">node-us-west-2</td>
                <td class="py-1 px-2 text-[#FF3333]">REJECTED</td>
                <td class="py-1 px-2 text-right">0.5KB</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

    </main>

    <!-- Right Column: Log Stream -->
    <aside class="w-80 bg-[#050505] p-3 flex flex-col font-code text-xs">
      <div class="mb-2 uppercase tracking-widest text-border-dim flex justify-between">
        <span>System Log Stream</span>
        <span class="text-amber animate-pulse">● LIVE</span>
      </div>
      <div class="flex-1 overflow-y-auto space-y-1">
        <div class="flex gap-2"><span class="text-border-dim">19:22:01</span><span class="text-amber">INFO</span><span class="text-white">GC_CYCLE_COMPLETE [120ms]</span></div>
        <div class="flex gap-2"><span class="text-border-dim">19:22:01</span><span class="text-amber">INFO</span><span class="text-white">TX_COMMIT 0x8F92...A1B2</span></div>
        <div class="flex gap-2"><span class="text-border-dim">19:22:00</span><span class="text-amber">INFO</span><span class="text-white">TX_COMMIT 0x4C21...9F0E</span></div>
        <div class="flex gap-2"><span class="text-border-dim">19:21:58</span><span class="text-amber">INFO</span><span class="text-white">TX_INIT 0x1A77...B89C</span></div>
        <div class="flex gap-2"><span class="text-border-dim">19:21:56</span><span class="text-amber">WARN</span><span class="text-white">MEM_SPIKE_DETECTED [8.4GB]</span></div>
        <div class="flex gap-2"><span class="text-border-dim">19:21:55</span><span class="text-amber">INFO</span><span class="text-white">TX_COMMIT 0x992B...33DF</span></div>
        <div class="flex gap-2"><span class="text-border-dim">19:21:52</span><span class="text-[#FF3333]">FAIL</span><span class="text-[#FF3333]">SIGKILL_RECEIVED node-us-west-2</span></div>
        <div class="flex gap-2"><span class="text-border-dim">19:21:52</span><span class="text-[#FF3333]">FAIL</span><span class="text-[#FF3333]">TX_REJECT 0x3E11...7A6D</span></div>
      </div>
    </aside>

  </div>
</body>
</html>
"""
