import React, { useState } from "react"
const CodeDebugger = () => {
  const [code, setCode] = useState("")
  const [isLoading, setIsLoading] = useState(false)
  const [debugged, setDebugged] = useState("")
  const [copied, setCopied] = useState(false)
  const [selectedLang, setSelectedLang] = useState("python")

  const languages = [
    { value: "python", label: "Python" },
    { value: "java", label: "Java" },
    { value: "c", label: "C" },
    { value: "cpp", label: "C++" },
    { value: "javascript", label: "JavaScript" },
    { value: "html", label: "HTML" },
    { value: "css", label: "CSS" },
  ]

  const handleDebug = async () => {
    setIsLoading(true)
    try {
      const response = await fetch("http://127.0.0.1:5000/response", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code: code, language: selectedLang }),
      })
      const result = await response.json()
      setDebugged(result.fixedCode || "// Error: " + (result.error || "Unknown"))
    } catch (err) {
      setDebugged("// Error: " + err.message)
    }
    setIsLoading(false)
  }
  const handleCopy = () => {
    if (navigator.clipboard) {
      navigator.clipboard.writeText(debugged).then(() => {
        setCopied(true)
        setTimeout(() => setCopied(false), 1500)
      })
    }
  }
  return (
    <div className="h-screen w-full grid grid-cols-2 gap-4 p-8 overflow-hidden">
      {/* Left Panel: Code Editor */}
      <div className="w-full p-6 bg-[#222222] rounded-md shadow-lg text-gray-200 flex flex-col">
        {/* Language Selector */}
        <select
          value={selectedLang}
          onChange={(e) => setSelectedLang(e.target.value)}
          className="bg-[#444444] p-2 mb-4 text-gray-100 rounded-md"
        >
          <optgroup label="Languages">
            {languages.map((lang) => (
              <option key={lang.value} value={lang.value}>
                {lang.label}
              </option>
            ))}
          </optgroup>
        </select>

        {/* Code Input */}
        <textarea
          value={code}
          onChange={(e) => setCode(e.target.value)}
          placeholder="Enter your code here..."
          className="w-full h-3/4 p-3 font-mono text-sm bg-[#444444] border border-gray-700 rounded-md resize-none placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-[#555555] text-gray-100"
        />
        <button
          onClick={handleDebug}
          disabled={isLoading}
          className={`mt-4 w-full py-2 rounded-md transition-colors ${
            isLoading
              ? "bg-blue-600 cursor-not-allowed text-gray-300"
              : "bg-blue-500 hover:bg-blue-600 text-white"
          }`}
        >
          {isLoading ? "Debugging..." : "Debug Code"}
        </button>
      </div>

      {/* Right Panel: Debug Output */}
      <div className="w-full p-6 bg-[#222222] rounded-md shadow-lg text-gray-200 flex flex-col relative">
        <label className="mb-2 text-gray-400">Debugged Code / Output:</label>
        <button
        onClick={handleCopy}
        title="Copy to clipboard"
        className="absolute top-2 right-8 p-2 rounded bg-blue-600 hover:bg-blue-700 text-white"
      >
        {copied ? '✓' : '📋'}
      </button>
        <textarea
          value={debugged}
          readOnly
          className="w-full h-full p-3 font-mono text-sm bg-[#444444] border border-gray-700 rounded-md resize-none placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-[#555555] text-gray-100"
        />
      </div>
    </div>
  )
}
export default CodeDebugger