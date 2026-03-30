# C Detector Documentation

The C detector is a lightweight, dependency-free implementation of the Phoenix Core detector in C.

## Building

### Requirements
- GCC or Clang compiler
- Standard C library

### Compilation
```bash
gcc simple_detector.c -o simple_detector
```

### Alternative Compilers
```bash
# Using Clang
clang simple_detector.c -o simple_detector

# With debugging symbols
gcc -g simple_detector.c -o simple_detector
```

## Usage

### Basic Usage
```bash
./simple_detector
```

### Interactive Commands
```
Press ENTER to capture, 'q' to quit
```

### Example Session
```
========================================
Phoenix Core - Simple C Detector
========================================
Press ENTER to capture, 'q' to quit

Capture? [ENTER]
  Photo captured (size: 1234567 bytes)
  Is this explicit? (y/n): y
  🔴 BLOCKED

  Statistics: 1 blocks / 1 captures (100.0%)

Capture? [ENTER]
  Photo captured (size: 1200000 bytes)
  Is this explicit? (y/n): n
  🟢 ALLOWED

  Statistics: 1 blocks / 2 captures (50.0%)

Capture? q
```

## Code Structure

### Main Components

#### 1. Capture Function
```c
snprintf(command, sizeof(command), "termux-camera-photo %s 2>/dev/null", photo_path);
system(command);
```
Uses Termux camera command to capture photos.

#### 2. Verification Loop
```c
while (1) {
    printf("Capture? ");
    fgets(input, sizeof(input), stdin);
    
    if (input[0] == 'q' || input[0] == 'Q') break;
```
Manual verification prompt.

#### 3. Statistics Tracking
```c
int block_count = 0;
int frame_count = 0;
```
Keeps running totals.

#### 4. File Operations
```c
snprintf(command, sizeof(command), "stat -c %%s %s", photo_path);
FILE *fp = popen(command, "r");
fscanf(fp, "%ld", &size);
```
Gets file size of captured images.

## Advantages

### Performance
- Minimal memory footprint (~2 MB)
- Fast startup (no Python interpreter)
- Direct system calls
- No dependency loading

### Portability
- Works anywhere GCC/Clang available
- No external libraries needed
- POSIX-compliant
- Cross-platform compatible

### Use Cases
1. **Embedded Systems**: Minimal dependencies
2. **Resource-Constrained Devices**: Very low memory
3. **Server Environments**: Background monitoring
4. **Testing**: Verify core blocking logic

## Output Explanation

### File Size
```
Photo captured (size: 1234567 bytes)
```
Size in bytes helps verify successful capture (typically 1-3 MB).

### Statistics
```
Statistics: 1 blocks / 1 captures (100.0%)
```
Format: `blocks / total (percentage)`

### Final Report
```
Final Statistics
Total captures: 10
Blocks: 3
Block rate: 30.0%
```
Summary after program ends.

## Customization

### Adding Logging

```c
FILE *log = fopen("debug.log", "a");
fprintf(log, "Frame %d: %s\n", frame_count, photo_path);
fclose(log);
```

### Changing Photo Path
```c
char photo_path[256] = "/sdcard/DCIM/Phoenix/photo.jpg";
```

### Modifying Prompts
```c
printf("Is this content acceptable? (y/n): ");
```

## Limitations

1. **Manual Verification**: User decides blocking
   - No automatic detection algorithm
   - Slower decision-making
   - Requires user attention

2. **No Image Analysis**: Only uses human judgment
   - Can't batch process
   - Not suitable for automation
   - Depends on user accuracy

3. **File-Based**: Creates temporary files
   - Disk I/O overhead
   - Storage usage
   - Cleanup required

## Integration

### Compile and Copy
```bash
gcc simple_detector.c -o simple_detector
cp simple_detector /usr/local/bin/
```

### Create Wrapper Script
```bash
#!/bin/bash
/usr/local/bin/simple_detector "$@"
```

### Background Monitoring
```bash
# Run in background
./simple_detector &
```

## Performance Considerations

### Memory Usage
- Stack: ~500 bytes
- Heap: ~1 KB
- Total: ~2 MB including system calls

### CPU Usage
- Idle: 0% (waiting for input)
- Active: 1-5% (I/O bound)

### Disk I/O
- Read: File stat operations
- Write: Temporary image files
- Delete: Cleanup after analysis

## Debugging

### Enable Verbose Output
Add this after captures:
```c
fprintf(stderr, "DEBUG: Processing %s\n", photo_path);
```

### Memory Leaks
```bash
gcc -g -fsanitize=address simple_detector.c -o simple_detector
./simple_detector
```

### Strace Monitoring
```bash
strace -e trace=file,read,write ./simple_detector
```

## Comparison with Python

| Aspect | C Detector | Python Scanner |
|--------|-----------|-----------------|
| Dependencies | None | NumPy, PIL |
| Memory | 2 MB | 30-50 MB |
| Speed | Fast | Medium |
| Automation | Manual | Automatic |
| Detection | Human | Algorithm |
| Learning Curve | Medium | Low |

## When to Use

### Use C Detector When:
- ✅ Minimal dependencies needed
- ✅ Very low memory available
- ✅ Manual verification acceptable
- ✅ Testing blocking logic
- ✅ Embedded systems

### Use Python Scanner When:
- ✅ Automatic detection needed
- ✅ Real-time processing required
- ✅ Statistics tracking important
- ✅ Vision algorithm accuracy matters
- ✅ Development/research

## Future Enhancements

Planned improvements:
- Image analysis libraries (libpng, libjpeg)
- Automatic detection algorithm
- SQLite logging
- Configuration files
- Multi-threading support

## Support

For issues with the C detector:
1. Check compilation errors: `gcc -Wall simple_detector.c`
2. Verify Termux setup: `termux-camera-photo test.jpg`
3. Report issues: GitHub Issues
4. Email: owiliberyll@gmail.com

## See Also

- [Main README](../README.md)
- [Scanner Documentation](scanners.md)
- [Termux Setup](termux-setup.md)
