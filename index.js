const { spawn } = require('child_process')
const fs = require('fs')

const imageBuffer = fs.readFileSync('./注册观众-钱五-123456.tif')

// 创建 Python 子进程
// const pythonProcess = spawn('convert.exe')
const pythonProcess = spawn('python', ['convert.py'])

// 将JSON字符串作为输入参数写入Python子进程的标准输入流中
pythonProcess.stdin.write(imageBuffer)
pythonProcess.stdin.end()

// 监听Python子进程的标准输出流，读取并处理返回结果
let result = Buffer.from('')
pythonProcess.stdout.on('data', data => {
  result = Buffer.concat([result, data])
})

pythonProcess.stdout.on('end', () => {
  // 在这里处理返回结果
  // console.log(result.toString())
  // console.log('result:', result)
  // console.log('end')
  fs.writeFileSync('注册观众-钱五-123456.24.tif', result)
})

pythonProcess.stderr.on('data', error => {
  console.error(error.toString())
})
