using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BuildHelper.Core
{
    public enum ELogType
    {
        INFO,
        WARNING,
        ERROR,
    }

    internal class Logger
    {
        public static readonly Logger Instance = new Logger();

        public void Log(string InMessage, ELogType InType = ELogType.INFO)
        {
            switch (InType)
            {
                case ELogType.INFO:
                    Console.ForegroundColor = ConsoleColor.Green;
                    break;
                case ELogType.WARNING:
                    Console.ForegroundColor = ConsoleColor.Yellow;
                    break;
                case ELogType.ERROR:
                    Console.ForegroundColor = ConsoleColor.Red;
                    break;
            }
            // 타입에만 색상 적용.
            Console.Write($"[{InType.ToString()}]");
            Console.ResetColor();

            Console.WriteLine($"::[{DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss")}]::[message : {InMessage}]");
        }
    }
}
