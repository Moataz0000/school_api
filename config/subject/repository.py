from .models import Subject



class SubjectRepo:
    
    @staticmethod
    def get_subject_by_id(pk):
        return Subject.objects.get(id=pk)
    
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

    @staticmethod
    def modify_subject(pk: int, title: str, is_active: bool):
        subject = Subject.objects.get(id=pk)
        subject.title = title
        subject.is_active = is_active
        subject.save()
        return subject