#!/usr/bin/env node
/**
 * LOGICAL BRUTALISM :: NODE WRAPPER
 * Ponte de execução para invocar o núcleo Python a partir de ambientes Node (NPM).
 */
const { spawn } = require('child_process');
const path = require('path');

const pyScript = path.join(__dirname, 'lb_init.py');

// Detecção agnóstica de runtime Python dependendo do SO alvo
const command = process.platform === 'win32' ? 'python' : 'python3';

const pyProcess = spawn(command, [pyScript, ...process.argv.slice(2)], { 
    stdio: 'inherit' 
});

pyProcess.on('close', (code) => {
    process.exit(code);
});

pyProcess.on('error', (err) => {
    console.error(`[SYS_ERR] Failed to execute Python engine: ${err.message}`);
    process.exit(1);
});
