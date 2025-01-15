import os
import ffmpeg

def convert_vob_to_mp4(input_path, output_path):
    """
    Converte um arquivo VOB para MP4 usando FFmpeg.
    """
    try:
        (
            ffmpeg
            .input(input_path)
            .output(output_path, vcodec='libx264', acodec='aac', strict='experimental')
            .run(overwrite_output=True)
        )
        print(f"Conversão concluída: {output_path}")
    except ffmpeg.Error as e:
        print(f"Erro durante a conversão: {e}")
        return False

def main():
    input_folder = 'videos'
    output_folder = 'output'

    # Certifique-se de que as pastas existem
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Lista todos os arquivos na pasta "videos"
    files = [f for f in os.listdir(input_folder) if f.lower().endswith('.vob')]

    if not files:
        print("Nenhum arquivo .vob encontrado na pasta 'videos'.")
        return

    for file in files:
        input_path = os.path.join(input_folder, file)
        output_file = f"{os.path.splitext(file)[0]}.mp4"
        output_path = os.path.join(output_folder, output_file)

        print(f"Convertendo {file} para {output_file}...")
        convert_vob_to_mp4(input_path, output_path)

if __name__ == "__main__":
    main()
