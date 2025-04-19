using System;
using System.Runtime.InteropServices;
using System.Text;

namespace BuildHelper.Core
{
    class IniFile
    {
        private string TargetFilePath;

        // INI 파일 경로를 생성자에서 받음
        public IniFile(string InPath)
        {
            TargetFilePath = InPath;
        }

        // INI에서 값 읽기
        [DllImport("kernel32", CharSet = CharSet.Auto, SetLastError = true)]
        private static extern int GetPrivateProfileString(
            string section,
            string key,
            string defaultValue,
            StringBuilder returnValue,
            int size,
            string filePath);

        // INI에 값 쓰기
        [DllImport("kernel32", CharSet = CharSet.Auto, SetLastError = true)]
        private static extern bool WritePrivateProfileString(
            string section,
            string key,
            string value,
            string filePath);

        // 키-값 읽기
        public string Read(string section, string key, string defaultValue = "")
        {
            StringBuilder result = new StringBuilder(255);
            GetPrivateProfileString(section, key, defaultValue, result, result.Capacity, TargetFilePath);
            return result.ToString();
        }

        // 키-값 쓰기
        public bool Write(string section, string key, string value)
        {
            return WritePrivateProfileString(section, key, value, TargetFilePath);
        }

        // 키 삭제
        public bool DeleteKey(string section, string key)
        {
            return WritePrivateProfileString(section, key, null, TargetFilePath);
        }

        // 섹션 삭제
        public bool DeleteSection(string section)
        {
            return WritePrivateProfileString(section, null, null, TargetFilePath);
        }
    }
}
