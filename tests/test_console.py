#!/usr/bin/node
/**
 * Test for the console
 */

const assert = require('assert');
const { describe, it, before, after, beforeEach, afterEach } = require('mocha');
const { createHBNBCommand, captureOutput, removeFile } = require('./testUtils'); // Assuming you have test utilities

describe('HBNBCommand', function () {
    let consol;

    before(function () {
        consol = createHBNBCommand();
    });

    after(function () {
        removeFile('file.json');
    });

    it('should pass PEP8 check', function () {
        const pep8Result = consol.runCommand('pep8 console.py');
        assert.strictEqual(pep8Result, '', 'Fix PEP8 issues');
    });

    describe('Docstrings', function () {
        const methods = [
            'emptyline',
            'do_quit',
            'do_EOF',
            'do_create',
            'do_show',
            'do_destroy',
            'do_all',
            'do_update',
            'count',
            'strip_clean',
            'default'
        ];

        methods.forEach(method => {
            it(`should have a docstring for ${method}`, function () {
                const docstring = consol.runCommand(`help ${method}`);
                assert(docstring.trim().length > 0, `Docstring missing for ${method}`);
            });
        });
    });

    describe('Command Handling', function () {
        beforeEach(function () {
            consol.resetOutput();
        });

        it('should handle empty line input', function () {
            consol.runCommand('\n');
            assert.strictEqual(consol.getOutput(), '');
        });

        // Add more tests for other commands
    });

    // Add more test cases as needed
});

// Add additional test helper functions if required
