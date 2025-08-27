<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>CSV Uploader · Region Selector</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root{ --bg:#0b0f14; --card:#121923; --muted:#9fb0c0; --text:#e6edf3; --accent:#5cc8ff; --accent2:#78f094; --border:#1f2a37; }
    *{box-sizing:border-box}
    html,body{height:100%}
    body{margin:0; font-family:Inter, system-ui, -apple-system, Segoe UI, Roboto, "Helvetica Neue", Arial, "Apple Color Emoji","Segoe UI Emoji"; background:linear-gradient(180deg,#0b0f14, #0d1520 40%, #0b0f14); color:var(--text);} 
    .container{max-width:1100px; margin:40px auto; padding:0 20px}
    .header{display:flex; align-items:center; justify-content:space-between; gap:16px; margin-bottom:24px}
    .title{font-size:clamp(20px, 2.5vw, 32px); font-weight:700; letter-spacing:.2px;}
    .card{background:var(--card); border:1px solid var(--border); border-radius:16px; padding:20px; box-shadow:0 10px 30px rgba(0,0,0,.25)}
    .grid{display:grid; grid-template-columns:1fr; gap:16px}
    @media(min-width:880px){.grid{grid-template-columns: 1.2fr .8fr}}
    .drop{border:2px dashed #2a3a4a; border-radius:14px; padding:26px; text-align:center; transition:.2s border-color, .2s background}
    .drop.dragover{border-color:var(--accent); background:rgba(92,200,255,.05)}
    .muted{color:var(--muted)}
    .controls{display:flex; flex-wrap:wrap; gap:12px; align-items:center}
    label{font-weight:600; font-size:14px}
    select, input[type="file"], button{background:#0e1621; color:var(--text); border:1px solid var(--border); border-radius:12px; padding:10px 12px; font-size:14px}
    select:focus, input[type="file"]:focus, button:focus{outline:2px solid var(--accent)}
    button{cursor:pointer; font-weight:600}
    button.primary{background:linear-gradient(180deg,#0e2433,#0c1f2b); border-color:#1e2a36}
    table{width:100%; border-collapse:collapse; font-size:14px}
    th, td{border-bottom:1px solid #1b2633; padding:10px; text-align:left;}
    th{position:sticky; top:0; background:#0f1722; z-index:1}
    .pill{display:inline-flex; align-items:center; gap:8px; background:#0f1b28; border:1px solid #1e2a36; padding:8px 12px; border-radius:999px}
    .sr-only{position:absolute; width:1px; height:1px; padding:0; margin:-1px; overflow:hidden; clip:rect(0,0,0,0); white-space:nowrap; border:0}
    .footer{margin-top:20px; display:flex; gap:10px; flex-wrap:wrap}
    .hint{font-size:12px; color:#9fb0c0}
    .error{color:#ff8e8e}
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div class="title">CSV Uploader & Region Selector</div>
      <div class="pill" aria-live="polite" id="statusPill">No file selected</div>
    </div>

    <div class="card grid" role="region" aria-labelledby="uploader-heading">
      <div>
        <h2 id="uploader-heading" class="sr-only">Upload CSV</h2>
        <div id="dropZone" class="drop" tabindex="0" aria-label="Drop CSV file here or use the file picker">
          <p><strong>Drag & drop</strong> your CSV here</p>
          <p class="muted">or</p>
          <input id="fileInput" type="file" accept=".csv,text/csv" aria-label="Choose CSV file" />
          <p class="hint">Only .csv files. Max preview: first 100 rows.</p>
          <p id="errorMsg" class="error" role="alert" hidden></p>
        </div>
      </div>

      <div>
        <h3 style="margin:0 0 8px 0">Options</h3>
        <div class="controls">
          <div style="display:flex; flex-direction:column; gap:6px; min-width:220px">
            <label for="regionSelect">Select region</label>
            <select id="regionSelect" aria-label="Region selector">
              <option value="">— Choose a region —</option>
              <option value="anz">anz</option>
              <option value="korea">korea</option>
              <option value="mena">mena</option>
              <option value="japan">japan</option>
              <option value="china">china</option>
            </select>
          </div>
          <div style="display:flex; gap:10px; align-items:center; margin-top:8px">
            <!-- Only one send option remains -->
            <button id="sendJsonBtn" class="primary" disabled>Generate Sentiment Summary</button>
          </div>
        </div>
      </div>
    </div>

    <div id="previewCard" class="card" style="margin-top:20px; display:none" aria-live="polite">
      <h3 style="margin-top:0">Preview</h3>
      <div id="meta" class="hint" style="margin-bottom:10px"></div>
      <div style="max-height:420px; overflow:auto">
        <table id="previewTable" aria-label="CSV preview table">
          <thead></thead>
          <tbody></tbody>
        </table>
      </div>
    </div>

    <div class="footer">
      <span class="hint">Your data stays in the browser unless you click <em>Send JSON to n8n</em>, which will POST parsed JSON rows (with region) to the hard‑coded webhook.</span>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/papaparse@5.4.1/papaparse.min.js" crossorigin="anonymous"></script>
  <script>
    (function(){
      // Hard-coded production webhook per request
      const WEBHOOK = 'https://corp-dev-aiplatform-n8n.data.ea.com/webhook/b89ebd73-ae38-46ff-9f8d-c66b2bed6ab1';

      const fileInput = document.getElementById('fileInput');
      const dropZone = document.getElementById('dropZone');
      const sendJsonBtn = document.getElementById('sendJsonBtn');
      const regionSelect = document.getElementById('regionSelect');
      const previewCard = document.getElementById('previewCard');
      const previewTable = document.getElementById('previewTable');
      const meta = document.getElementById('meta');
      const statusPill = document.getElementById('statusPill');
      const errorMsg = document.getElementById('errorMsg');

      let originalRows = [];
      let originalMeta = { delimiter: ',', header: true };
      let filename = null;

      function setStatus(text){ statusPill.textContent = text; }
      function setError(msg){ errorMsg.textContent = msg; errorMsg.hidden = !msg; }

      function enableControls(){
        const hasFile = !!filename;
        const hasRegion = !!regionSelect.value;
        sendJsonBtn.disabled = !(hasFile && hasRegion);
      }

      regionSelect.addEventListener('change', enableControls);

      function handleFiles(files){
        setError('');
        const file = files && files[0];
        if(!file) return;
        if(!file.name.toLowerCase().endsWith('.csv')){ setError('Please choose a .csv file.'); return; }
        filename = file.name; setStatus(file.name);

        Papa.parse(file, {
          header: true,
          skipEmptyLines: 'greedy',
          transformHeader: h => h.replace(/^\uFEFF/, '').trim(), // strip BOM + trim
          complete: function(results){
            // drop fully empty rows
            const clean = (results.data || []).filter(r => r && Object.values(r).some(v => String(v ?? '').trim() !== ''));
            originalRows = clean;
            originalMeta = results.meta || originalMeta;
            enableControls();
            renderPreview();
          },
          error: function(err){ setError('Parse error: ' + err.message); }
        });
      }

      // Drag & drop
      ['dragenter','dragover'].forEach(evt => dropZone.addEventListener(evt, e=>{ e.preventDefault(); e.stopPropagation(); dropZone.classList.add('dragover'); }));
      ['dragleave','drop'].forEach(evt => dropZone.addEventListener(evt, e=>{ e.preventDefault(); e.stopPropagation(); dropZone.classList.remove('dragover'); }));
      dropZone.addEventListener('drop', (e)=>{ handleFiles(e.dataTransfer.files); });
      dropZone.addEventListener('keydown', (e)=>{ if(e.key==='Enter' || e.key===' '){ fileInput.click(); }});

      // File picker
      fileInput.addEventListener('change', (e)=> handleFiles(e.target.files));

      // Send JSON button
      sendJsonBtn.addEventListener('click', (e)=>{ e.preventDefault(); sendToN8N_JSON_Fixed(); });

      function renderPreview(){
        if(!Array.isArray(originalRows) || originalRows.length === 0){ setError('No rows found in this CSV.'); return; }
        setError(''); previewCard.style.display = 'block';

        const columns = Object.keys(originalRows[0]);
        const thead = previewTable.querySelector('thead');
        const tbody = previewTable.querySelector('tbody');
        thead.innerHTML = ''; tbody.innerHTML = '';

        const trh = document.createElement('tr');
        columns.forEach(col => { const th = document.createElement('th'); th.textContent = col; trh.appendChild(th); });
        thead.appendChild(trh);

        const MAX = 100;
        originalRows.slice(0, MAX).forEach(row =>{
          const tr = document.createElement('tr');
          columns.forEach(col =>{ const td = document.createElement('td'); const v = row[col]; td.textContent = (v===undefined || v===null) ? '' : String(v); tr.appendChild(td); });
          tbody.appendChild(tr);
        });

        meta.textContent = `Rows: ${originalRows.length.toLocaleString()} · Columns: ${columns.length} · Delimiter: "${originalMeta.delimiter || ','}"`;
      }

      // Send parsed JSON rows with region to fixed webhook
      async function sendToN8N_JSON_Fixed(){
        if(!regionSelect.value){ setError('Select a region.'); return; }

        // If no parsed rows yet, try parsing now with delimiter fallbacks
        if(originalRows.length === 0){
          const file = fileInput.files && fileInput.files[0];
          if(file){
            const tryParse = (delimiter) => new Promise((resolve, reject) => {
              Papa.parse(file, {
                header: true,
                skipEmptyLines: 'greedy',
                delimiter: delimiter || '', // '' lets Papa auto-detect
                transformHeader: h => h.replace(/^\uFEFF/, '').trim(),
                complete: ({ data, meta }) => {
                  const clean = (data || []).filter(r => r && Object.values(r).some(v => String(v ?? '').trim() !== ''));
                  resolve({ rows: clean, meta });
                },
                error: (err) => reject(err)
              });
            });

            try{
              let parsed = await tryParse('');          // auto-detect
              if(parsed.rows.length === 0) parsed = await tryParse(';');  // semicolon
              if(parsed.rows.length === 0) parsed = await tryParse('\t'); // tab-separated
              originalRows = parsed.rows;
              originalMeta = parsed.meta || originalMeta;
              if(originalRows.length === 0){ setError('No data detected in the CSV. Check the delimiter or file contents.'); return; }
              renderPreview();
            }catch(e){ setError('Parse error: ' + e.message); return; }
          }
        }

        if(originalRows.length === 0){ setError('No data to send.'); return; }

        const region = regionSelect.value.trim().toLowerCase();
        const rows = originalRows.map(r => {
          const out = { ...r };
          for (const k in out) if (out[k] === undefined || out[k] === null) out[k] = '';
          out['region'] = region;
          return out;
        });

        const payload = {
          rows,
          meta: {
            filename: filename || 'upload.csv',
            columns: rows.length ? Object.keys(rows[0]) : [],
            delimiter: (originalMeta && originalMeta.delimiter) ? originalMeta.delimiter : ','
          }
        };

        try{
          const res = await fetch(WEBHOOK, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
          });
          const text = await res.text();
          if(!res.ok){ setError('n8n error: ' + text); return; }
          alert(`Sent ${rows.length} JSON rows to n8n ✅`);
        }catch(err){ console.error(err); setError('Network error sending JSON to n8n. Check CORS and the URL.'); }
      }

      // Initialize
      enableControls();
    })();
  </script>
</body>
</html>
