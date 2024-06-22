from rest_framework import permissions

# для глобального исопльзования пермишенов пользуеемся  settings. Но


class AdminOrReadOnly(permissions.BasePermission):  #свйо класс пермишшенов

    def has_permission(self, request, view):  # куда етсь доступ
        if request.method in permissions.SAFE_METHODS:  # если метод безопасный get, head, option
            return True

        return bool(request.user and request.user.is_staff)


class IsOwnerOrRadOnly(permissions.BasePermission):   #свйо класс пермишшенов что бы все читали, а владелец удалял

    def has_object_permission(self, request, view, obj):  # куда етсь доступ
        if request.method in permissions.SAFE_METHODS:  # если метод безопасный get, head, option
            return True

        return obj.user == request.user
