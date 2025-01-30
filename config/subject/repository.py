from .models import Subject



class SubjectRepo:
    
    @staticmethod
    def get_all_avaliable_subject():
        return Subject.objects.filter(is_active=True)
    
    @staticmethod
    def add_subject(title: str, is_active: bool = True):
        subject, _ = Subject.objects.get_or_create(
            title=title,
            defaults={"is_active": is_active}
        )
        return subject