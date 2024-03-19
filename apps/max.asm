section .text
global max_pts

max_pts:
    ;; creating stack frame
    push ebp
    mov ebp, esp

    ;; init FPU
    finit 

    fld dword[ebp + 12] ; Carregar 'b' na pilha de ponto flutuante
    fld dword[ebp + 8] ; Carregar 'a' na pilha de ponto flutuante

    fcomi st1
    jbe swap ; se 'st1' não for maior, pular para 'swap'
    jmp end
swap:
    fxch st1 ; troca os valores de st0 e st1
end:
    ;;destroying stack frame
    mov esp, ebp
    pop ebp

    ret