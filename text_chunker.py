# text_chunker.py

class TextChunker:

    def __init__(
        self,
        chunk_size=500,
        overlap=50
    ):
        if overlap >= chunk_size:
            raise ValueError("overlap must be smaller than chunk_size")

        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk_text(self, paragraphs):
        """
        Convert paragraphs into overlapping chunks.
        """

        full_text = "\n".join(paragraphs)

        chunks = []

        start = 0

        while start < len(full_text):

            end = start + self.chunk_size

            chunk = full_text[start:end]

            chunks.append(chunk)

            start += self.chunk_size - self.overlap

        return chunks