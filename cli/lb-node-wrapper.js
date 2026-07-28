#!/usr/bin/env node
/**
 * LOGICAL BRUTALISM :: NODE WRAPPER
 * Execution bridge to invoke the Python CLI engine from Node environments (NPM).
 * Uses `-m` flag for proper module resolution across subcommands.
 */
const { spawn } = require('child_process');
const path = require('path');

// Package root (parent of cli/)
const pkgRoot = path.join(__dirname, '..');

// OS-agnostic Python runtime detection
const command = process.platform === 'win32' ? 'python' : 'python3';

// Execute as module for proper import resolution (cli.commands, cli.payloads)
const pyProcess = spawn(command, ['-m', 'cli.lb_init', ...process.argv.slice(2)], { 
    stdio: 'inherit',
    cwd: pkgRoot,
});

pyProcess.on('close', (code) => {
    process.exit(code);
});

pyProcess.on('error', (err) => {
    console.error(`[SYS_ERR] Failed to execute Python engine: ${err.message}`);
    process.exit(1);
});
