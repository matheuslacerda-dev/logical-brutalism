#!/usr/bin/env node
/**
 * LOGICAL BRUTALISM :: NODE WRAPPER
 * Execution bridge to invoke the Python core from Node environments (NPM).
 */
const { spawn } = require('child_process');
const path = require('path');

const pyScript = path.join(__dirname, 'lb_init.py');

// OS-agnostic Python runtime detection
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
