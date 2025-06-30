@echo off
echo.
echo =====================================================
echo   Sistema de Gestion de Anuncios Publicitarios
echo             Aplicacion Web con Flask
echo =====================================================
echo.

echo Verificando requisitos...
python init_web.py

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ¿Deseas iniciar la aplicacion web ahora? (S/N)
    set /p respuesta=
    
    if /i "%respuesta%"=="S" (
        echo.
        echo Iniciando aplicacion web...
        echo Accede a: http://localhost:5000
        echo Presiona Ctrl+C para detener
        echo.
        python app.py
    ) else (
        echo.
        echo Para iniciar manualmente ejecuta: python app.py
    )
) else (
    echo.
    echo Error en la inicializacion. Revisa los mensajes anteriores.
    pause
)
