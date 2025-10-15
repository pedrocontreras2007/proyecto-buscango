from plyer import notification

class Notificador:
    @staticmethod
    def enviar_alerta(titulo, mensaje):
        try:
            notification.notify(
                title=titulo,
                message=mensaje,
                app_icon=None,
                timeout=10
            )
        except Exception as e:
            print(f"Error al enviar notificación: {e}")